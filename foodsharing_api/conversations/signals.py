from django.db.models.signals import post_save

from foodsharing_api.conversations.models import ConversationMessage

def update_last_message(sender, instance, **kwargs):
    instance.conversation.last_message = instance
    instance.conversation.save()

post_save.connect(update_last_message, sender=ConversationMessage)