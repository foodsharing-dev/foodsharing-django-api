"""Define the api for the conversation app"""
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.conversations.serializers import ConversationListSerializer
from foodsharing_api.conversations.serializers import ConversationRetrieveSerializer
from foodsharing_api.conversations.models import Conversation as ConversationModel

class ConversationPagination(LimitOffsetPagination):
    """Paginator for the conversation"""
    default_limit = 50
    max_limit = 1000


class ConversationViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        GenericViewSet
):
    """
    Conversations
    """
    queryset = ConversationModel.objects
    pagination_class = ConversationPagination
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        serializer_class = None
        if self.action in ('retrieve', ):
            serializer_class = ConversationRetrieveSerializer
        elif self.action in ('list', ):
            serializer_class = ConversationListSerializer
        return serializer_class

    def get_queryset(self):
        return self.queryset.filter(members=self.request.user).\
            order_by('-last_message_id').\
            prefetch_related('members', 'last_message', 'last_message__sent_by')
