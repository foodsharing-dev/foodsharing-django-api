"""Models for the Pickup app"""

from django.db import models

from foodsharing_api.stores.models import Store
from foodsharing_api.users.models import User


class TakenPickup(models.Model):
    """Pickup Model"""
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='foodsaver_id')
    store = models.ForeignKey(Store, models.DO_NOTHING, db_column='betrieb_id')
    at = models.DateTimeField(db_column='date')
    confirmed = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'fs_abholer'
        unique_together = (('user', 'store', 'at'),)
