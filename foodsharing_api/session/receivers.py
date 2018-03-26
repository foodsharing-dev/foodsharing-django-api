"""Receivers for the session app"""
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from django_redis import get_redis_connection


@receiver(user_logged_in)
def add_session_to_user_session_map(sender, request, user, **kwargs):
    """Adding the session to redis"""
    if user:
        redis = get_redis_connection(settings.SESSION_CACHE_ALIAS)
        redis.sadd(
            'api:user:{}:sessions'.format(user.id),
            request.session.session_key
        )

@receiver(user_logged_out)
def remove_session_from_user_session_map(sender, request, user, **kwargs):
    """Remove the session from redis"""
    if user:
        redis = get_redis_connection(settings.SESSION_CACHE_ALIAS)
        redis.srem(
            'api:user:{}:sessions'.format(user.id),
            request.session.session_key
        )
