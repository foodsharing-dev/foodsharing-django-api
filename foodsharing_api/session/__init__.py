"""Session App configuration"""

from django.apps import AppConfig

class SessionConfig(AppConfig):
    """Configuration for the session app"""
    name = 'foodsharing_api.session'

    def ready(self):
        """import the receivers after the app is ready"""
        from . import receivers
