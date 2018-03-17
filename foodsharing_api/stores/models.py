"""
Models for the stores app
"""
from datetime import date

from django.db import models
from enumfields import Enum, EnumIntegerField

from foodsharing_api.users.models import User as UserModel
from foodsharing_api.conversations.models import Conversation as ConversationModel

class StoreTeam(models.Model):
    """Model for the store team members"""
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        db_column='foodsaver_id'
    )
    store = models.ForeignKey(
        'stores.Store',
        db_column='betrieb_id',
        on_delete=models.CASCADE,
        related_name='team_set'
    )
    coordinator = models.BooleanField(db_column='verantwortlich')
    active = models.IntegerField(default=0)
    stat_last_update = models.DateTimeField(null=True)
    stat_fetchcount = models.IntegerField(default=0)
    stat_first_fetch = models.DateField(null=True)
    stat_last_fetch = models.DateTimeField(null=True)
    stat_add_date = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = 'fs_betrieb_team'
        unique_together = (('user', 'store'),)


class EstimatedFetchTime(Enum):
    """Enumeration of the pickup times"""
    NONE = 0
    MORNING = 1
    NOON = 2
    EVENING = 3
    NIGHT = 4


class Conviction(Enum):
    """Enumeration of conviction levels"""
    NONE = 0
    EASY = 1
    MEDIUM = 2
    DIFFICULT = 3
    NEARLY_IMPOSSIBLE = 4


class TeamStatus(Enum):
    """Enumeration of teams states"""
    FULL = 0
    OPEN = 1
    IN_NEED = 2

class Status(Enum):
    """Enumeration of states"""
    NONE = 0
    NO_CONTACT = 1
    NEGOTIATING = 2
    RUNNING = 3
    DECLINED = 4
    THIRD_PARTY_COOPERATION = 5
    CHARITY_NO_WASTE = 6


class Store(models.Model):
    """Model for the store"""
    status = EnumIntegerField(
        Status,
        db_column='betrieb_status_id',
        default=Status.NO_CONTACT
    )
    district = models.IntegerField(db_column='bezirk_id', default=0)
    created_at = models.DateField(db_column='added', default=date.today)
    zip = models.CharField(max_length=5, db_column='plz')
    city = models.CharField(max_length=50, db_column='stadt')
    lat = models.CharField(max_length=20, blank=True, null=True)
    lon = models.CharField(max_length=20, blank=True, null=True)
    store_chain = models.IntegerField(
        blank=True,
        null=True,
        db_column='kette_id'
    )
    name = models.CharField(max_length=120, blank=True, null=True)
    street = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        db_column='str'
    )
    house_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_column='hsnr'
    )
    status_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        db_column='telefon'
    )
    email = models.CharField(max_length=60, blank=True, null=True)
    cooperation_started_at = models.DateField(
        blank=True,
        null=True,
        db_column='begin'
    )
    notes = models.TextField(blank=True, null=True, db_column='besonderheiten')
    notes_public = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        db_column='public_info'
    )
    estimated_fetch_time = EnumIntegerField(
        EstimatedFetchTime,
        db_column='public_time',
        default=EstimatedFetchTime.NONE
    )
    conviction = EnumIntegerField(
        Conviction,
        db_column='ueberzeugungsarbeit',
        default=Conviction.NONE
    )
    name_in_press_ok = models.IntegerField(db_column='presse', default=0)
    put_sticker_ok = models.IntegerField(db_column='sticker', default=0)
    average_fetch_weight = models.IntegerField(
        db_column='abholmenge',
        default=0
    )
    team_status = EnumIntegerField(TeamStatus, default=TeamStatus.OPEN)
    pickup_signup_advance = models.IntegerField(
        db_column='prefetchtime',
        default=1209600
    )
    team_conversation = models.ForeignKey(
        ConversationModel,
        db_column='team_conversation_id',
        related_name='+'
    )
    waiter_conversation = models.ForeignKey(
        ConversationModel,
        db_column='springer_conversation_id',
        related_name='+'
    )
    deleted_at = models.DateTimeField(blank=True, null=True)
    team = models.ManyToManyField(UserModel, through='StoreTeam')

    class Meta:
        managed = False
        db_table = 'fs_betrieb'
