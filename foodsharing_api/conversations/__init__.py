from django.apps import AppConfig

class ConversationsConfig(AppConfig):
    name = 'foodsharing_api.conversations'

    def ready(self):
        from . import signals