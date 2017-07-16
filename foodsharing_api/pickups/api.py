import datetime

from django.db.models import Count
from django.http import Http404
from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.pickups.serializers import TakenPickupSerializer, PickupSerializer
from foodsharing_api.pickups.models import TakenPickup as TakenPickupModel
from foodsharing_api.utils.decorators import setup_eager_loading

class IsMember(BasePermission):
    message = ('You are not a member of this store.')

    def has_object_permission(self, request, view, obj):
        found = False
        for m in obj.store.team.all():
            if m.id == request.user.id:
                found = True
        return found


class PickupViewSet(
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    """
    Pickups
    """
    serializer_class = TakenPickupSerializer
    queryset = TakenPickupModel.objects
    permission_classes = (IsMember,)

    @list_route(['GET'])
    def next(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset.filter(user=self.request.user).filter(at__gt=datetime.datetime.now() - datetime.timedelta(hours=2)).order_by('at'))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TakenPickupSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TakenPickupSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action=='retrieve':
            serializer_class = PickupSerializer
        return serializer_class

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {'store': self.kwargs['store'], 'at': self.kwargs['at']}
        res = queryset.filter(**filter_kwargs).select_related('user')

        obj = res.first()
        if obj is None:
            raise Http404

        obj.members = []
        for r in res:
            u = r.user
            u.confirmed = r.confirmed
            obj.members.append(u)

        self.check_object_permissions(self.request, obj)

        return obj


    def get_queryset(self):
        if self.action=='retrieve':
            return self.queryset


