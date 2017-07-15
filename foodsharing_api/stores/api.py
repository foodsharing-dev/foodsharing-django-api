from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.stores.serializers import StoreSerializer
from foodsharing_api.stores.models import Store as StoreModel
from foodsharing_api.utils.decorators import setup_eager_loading


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

    @setup_eager_loading
    def get_queryset(self):
        return self.queryset.filter(team=self.request.user).all().prefetch_related('team')