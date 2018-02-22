"""
Serializers for the stores app
"""
from rest_framework import serializers

from foodsharing_api.stores.models import Store as StoreModel
from foodsharing_api.stores.models import StoreTeam as StoreTeamModel
from foodsharing_api.users.serializers import UserSerializer
from foodsharing_api.users.models import User as UserModel

class StoreUserSerializer(UserSerializer):
    """Store user serializer"""
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'photo', 'phone', 'mobile']

class StoreTeamSerializer(serializers.ModelSerializer):
    """Serializer for the store team"""
    user = StoreUserSerializer()
    class Meta:
        model = StoreTeamModel
        fields = ['user', 'coordinator']

    # flatten a subfield, e.g. here: user
    def to_representation(self, instance):

        representation = super().to_representation(instance)
        sub_representation = representation.pop('user')
        if sub_representation:
            for key in sub_representation:
                representation[key] = sub_representation[key]

        return representation

class StoreSerializer(serializers.ModelSerializer):
    """Store serializer"""
    team = StoreTeamSerializer(many=True, source='team_set')

    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related(
            'team_set',
            'team',
            'team_set__user'
        )

        return queryset

    class Meta:
        model = StoreModel
        fields = [
            'id',
            'name',
            'street',
            'house_number',
            'zip',
            'city',
            'notes',
            'team_conversation',
            'team'
        ]
