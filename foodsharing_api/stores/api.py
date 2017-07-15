from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.stores.serializers import StoreSerializer
from foodsharing_api.stores.models import Store as StoreModel


class StoreViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    Stores
    """
    serializer_class = StoreSerializer
    queryset = StoreModel.objects.filter(deleted_at=None)

    def get_queryset(self):
        return self.queryset.filter(team=self.request.user)