"""App to handle the conversation"""
from django.apps import AppConfig

class ConversationsConfig(AppConfig):
    """Configuration for the Converstation app"""
    name = 'foodsharing_api.conversations'

    def ready(self):
        """Importing and register the signals for the app"""
        from . import signals
