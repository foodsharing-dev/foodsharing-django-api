"""Factory for the user creation"""
from django.contrib.auth import get_user_model
from factory import DjangoModelFactory
from factory import CREATE_STRATEGY
from factory import PostGeneration
from factory import Faker


class UserFactory(DjangoModelFactory):
    """Factory for user creation"""
    class Meta:
        model = get_user_model()
        strategy = CREATE_STRATEGY

    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')

    verified = 1
    active = 1
    passwd = PostGeneration(
        lambda obj, *args, **kwargs: obj.set_password(obj.email)
    )
