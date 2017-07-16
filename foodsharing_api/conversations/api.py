from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.conversations.serializers import ConversationListSerializer, ConversationRetrieveSerializer
from foodsharing_api.conversations.models import Conversation as ConversationModel


class ConversationViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    Conversations
    """
    queryset = ConversationModel.objects

    def get_serializer_class(self):
        serializer_class = None
        if self.action in ('retrieve'):
            serializer_class = ConversationRetrieveSerializer
        elif self.action in ('list'):
            serializer_class = ConversationListSerializer
        return serializer_class

    def get_queryset(self):
        return self.queryset.filter(members=self.request.user).order_by('-last_message')
