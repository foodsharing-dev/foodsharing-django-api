"""Api for the pickup app"""

import datetime

from django.http import Http404
from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from foodsharing_api.pickups.serializers import TakenPickupSerializer
from foodsharing_api.pickups.serializers import PickupSerializer
from foodsharing_api.pickups.models import TakenPickup as TakenPickupModel

class IsMember(BasePermission):
    """Check if user is member of the given store"""

    message = ('You are not a member of this store.')

    def has_object_permission(self, request, view, obj):
        """Is the user a registered foodsaver for the store"""
        found = False
        for member in obj.store.team.all():
            if member.id == request.user.id:
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
        """Returns the next planned pickup of a user"""
        queryset = self.filter_queryset(
            self.queryset.filter(
                user=self.request.user
            ).filter(
                at__gt=datetime.datetime.now() - datetime.timedelta(hours=2)
            ).order_by('at')
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TakenPickupSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TakenPickupSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        """Sets the serializer for the pickup"""
        if self.action == 'retrieve':
            serializer_class = PickupSerializer
        return serializer_class

    def get_object(self):
        """Returns the pickup for the user for the store"""
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {'store': self.kwargs['store'], 'at': self.kwargs['at']}
        results = queryset.filter(**filter_kwargs).select_related('user', 'store')

        obj = results.first()
        if obj is None:
            raise Http404

        obj.members = []
        for result in results:
            u = result.user
            u.confirmed = result.confirmed
            obj.members.append(u)

        self.check_object_permissions(self.request, obj)

        return obj


    def get_queryset(self):
        """Returns the predefined QuerySet"""
        if self.action == 'retrieve':
            return self.queryset


