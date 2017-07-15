from rest_framework import serializers

from foodsharing_api.stores.models import Store as StoreModel
from foodsharing_api.stores.models import StoreTeam as StoreTeamModel
from foodsharing_api.users.serializers import UserSerializer


class StoreTeamSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = StoreTeamModel
        fields = ['user', 'coordinator']

class StoreSerializer(serializers.ModelSerializer):
    team = StoreTeamSerializer(many=True, source='team_set')

    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('team_set', 'team', 'team_set__user')

        return queryset

    class Meta:
        model = StoreModel
        fields = ['id', 'name', 'street', 'houseNumber', 'zip', 'city', 'notes', 'team_conversation', 'team']
