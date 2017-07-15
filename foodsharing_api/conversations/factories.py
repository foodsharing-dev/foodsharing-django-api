import datetime
from factory import DjangoModelFactory, CREATE_STRATEGY, post_generation, Faker
from foodsharing_api.conversations.models import Conversation as ConversationModel, ConversationMessage as ConversationMessageModel, ConversationMember as ConversationMemberModel


class ConversationFactory(DjangoModelFactory):
    class Meta:
        model = ConversationModel
        strategy = CREATE_STRATEGY

    name = Faker('name')

    @post_generation
    def members(self, created, members, **kwargs):
        if not created:
            return
        if members:
            for member in members:
                ConversationMemberModel.objects.create(conversation=self, user=member)


class ConversationMessageFactory(DjangoModelFactory):
    class Meta:
        model = ConversationMessageModel
        strategy = CREATE_STRATEGY

    body = Faker('text')
    sent_at = datetime.datetime.now()