"""Models for the conversation app"""
from django.db import models

from foodsharing_api.users.models import User



class Conversation(models.Model):
    """Model for a conversation"""
    locked = models.BooleanField(default=False)
    name = models.CharField(max_length=40, blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    last = models.DateTimeField(blank=True, null=True)
    last_user = models.ForeignKey(
        User,
        models.DO_NOTHING,
        db_column='last_foodsaver_id',
        related_name='conversations_with_last_participation'
    )
    start_user = models.ForeignKey(
        User,
        models.DO_NOTHING,
        db_column='start_foodsaver_id',
        related_name='started_conversations'
    )
    last_message = models.ForeignKey(
        'ConversationMessage',
        models.DO_NOTHING,
        db_column='last_message_id',
        related_name='conversation_with_last_message')
    last_message_body = models.TextField(null=True, db_column='last_message')
    member = models.TextField(null=True)
    members = models.ManyToManyField(User, through='ConversationMember')

    class Meta:
        managed = False
        db_table = 'fs_conversation'


class ConversationMessage(models.Model):
    """Model for a message"""
    conversation = models.ForeignKey(
        Conversation,
        models.DO_NOTHING,
        db_column='conversation_id',
        related_name='messages'
    )
    sent_by = models.ForeignKey(
        User,
        models.DO_NOTHING,
        db_column='foodsaver_id'
    )
    body = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True, db_column='time')

    class Meta:
        managed = False
        db_table = 'fs_msg'


class ConversationMember(models.Model):
    """Model for the members of a conversation"""
    user = models.ForeignKey(
        User,
        models.DO_NOTHING,
        db_column='foodsaver_id',
    )
    conversation = models.ForeignKey(
        Conversation,
        models.DO_NOTHING,
        db_column='conversation_id'
    )
    unread = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'fs_foodsaver_has_conversation'
        unique_together = (('user', 'conversation'),)
