from rest_framework import serializers

from foodsharing_api.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'photo']
