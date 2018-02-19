"""Factories for creating Conversations and Messages"""

from django.utils.timezone import now
from factory import DjangoModelFactory, CREATE_STRATEGY, post_generation, Faker
from foodsharing_api.conversations.models import Conversation as ConversationModel
from foodsharing_api.conversations.models import ConversationMessage as ConversationMessageModel
from foodsharing_api.conversations.models import ConversationMember as ConversationMemberModel


class ConversationFactory(DjangoModelFactory):
    """Factory for Conversation creation"""
    class Meta:
        model = ConversationModel
        strategy = CREATE_STRATEGY

    name = Faker('name')

    @post_generation
    def members(self, created, members, **kwargs):
        """Add existing members to th conversation"""
        if not created:
            return
        if members:
            for member in members:
                ConversationMemberModel.objects.create(
                    conversation=self,
                    user=member
                )


class ConversationMessageFactory(DjangoModelFactory):
    """Factory for message creation"""
    class Meta:
        model = ConversationMessageModel
        strategy = CREATE_STRATEGY

    body = Faker('text')
    sent_at = now()
