from datetime import datetime

from factory import DjangoModelFactory, CREATE_STRATEGY
from foodsharing_api.pickups.models import TakenPickup as TakenPickupModel
from foodsharing_api.stores.factories import StoreFactory
from foodsharing_api.users.models import User as UserModel

class TakenPickupFactory(DjangoModelFactory):
    class Meta:
        model = TakenPickupModel
        strategy = CREATE_STRATEGY

    user = UserModel.objects.first()
    at = datetime.now()
    store = StoreFactory()