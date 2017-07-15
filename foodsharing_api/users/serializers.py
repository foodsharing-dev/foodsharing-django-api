from rest_framework import serializers

from foodsharing_api.users.models import FsFoodsaver


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FsFoodsaver
        fields = ['id', 'name', 'email']
