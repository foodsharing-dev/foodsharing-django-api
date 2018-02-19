"""Define the serializers for the api"""
from rest_framework import serializers

from foodsharing_api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the foodsharing user"""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'photo']
