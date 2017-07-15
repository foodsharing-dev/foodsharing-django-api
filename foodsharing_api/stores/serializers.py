from rest_framework import serializers

from foodsharing_api.stores.models import Store as StoreModel
from foodsharing_api.stores.models import StoreTeam as StoreTeamModel

class StoreTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreTeamModel
        fields = ['user', 'coordinator']

class StoreSerializer(serializers.ModelSerializer):
    team = StoreTeamSerializer(many=True)
    class Meta:
        model = StoreModel
        fields = ['id', 'name', 'street', 'houseNumber', 'zip', 'city', 'notes', 'team_conversation']
