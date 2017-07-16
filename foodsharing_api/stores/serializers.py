from rest_framework import serializers

from foodsharing_api.stores.models import Store as StoreModel
from foodsharing_api.stores.models import StoreTeam as StoreTeamModel
from foodsharing_api.users.serializers import UserSerializer


class StoreTeamSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = StoreTeamModel
        fields = ['user', 'coordinator']

    # flatten a subfield, e.g. here: user
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        sub_representation = representation.pop('user')
        for key in sub_representation:
            representation[key] = sub_representation[key]

        return representation

class StoreSerializer(serializers.ModelSerializer):
    team = StoreTeamSerializer(many=True, source='team_set')

    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('team_set', 'team', 'team_set__user')

        return queryset

    class Meta:
        model = StoreModel
        fields = ['id', 'name', 'street', 'house_number', 'zip', 'city', 'notes', 'team_conversation', 'team']
