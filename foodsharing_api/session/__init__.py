from django.apps import AppConfig

class SessionConfig(AppConfig):
    name = 'foodsharing_api.session'

    def ready(self):
        from . import receivers
