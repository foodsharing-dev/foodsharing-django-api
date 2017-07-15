from django.db.migrations import serializer
from rest_framework import serializers

from foodsharing_api.conversations.models import ConversationMessage as ConversationMessageModel
from foodsharing_api.conversations.models import Conversation as ConversationModel
from foodsharing_api.users.serializers import UserSerializer


class ConversationMemberSerializer(UserSerializer):
    pass

class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessageModel
        fields = ['sent_by', 'sent_at', 'body']


class ConversationListSerializer(serializers.ModelSerializer):
    members = ConversationMemberSerializer(many=True)
    last_message = ConversationMessageSerializer()

    class Meta:
        model = ConversationModel
        fields = ['id', 'name', 'locked', 'last_message', 'members']


class ConversationRetrieveSerializer(ConversationListSerializer):
    messages = serializers.SerializerMethodField()
    #messages = ConversationMessageSerializer(many=True)

    def get_messages(self, instance):
        ordered_queryset = ConversationMessageModel.objects.filter(conversation_id=instance.id)\
            .order_by('-sent_at')
        return  ConversationMessageSerializer(ordered_queryset, many=True).data
    class Meta:
        model = ConversationModel
        fields = ['name', 'locked', 'messages', 'members']