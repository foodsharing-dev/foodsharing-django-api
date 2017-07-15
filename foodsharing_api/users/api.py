from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.users.models import FsFoodsaver
from foodsharing_api.users.serializers import UserSerializer


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    Users
    """
    queryset = FsFoodsaver.objects
    serializer_class = UserSerializer