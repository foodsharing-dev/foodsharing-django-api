from factory import Faker, DjangoModelFactory, CREATE_STRATEGY, post_generation
from foodsharing_api.stores.models import Store as StoreModel, StoreTeam as StoreTeamModel


class StoreFactory(DjangoModelFactory):
    class Meta:
        model = StoreModel
        strategy = CREATE_STRATEGY

    @post_generation
    def members(self, created, members, **kwargs):
        if not created:
            return
        if members:
            for member in members:
                StoreTeamModel.objects.create(store=self, user=member, coordinator=0, active=1)

    @post_generation
    def coordinators(self, created, coordinators, **kwargs):
        if not created:
            return
        if coordinators:
            for coordinator in coordinators:
                StoreTeamModel.objects.create(store=self, user=coordinator, coordinator=1, active=1)

    name = Faker('name')
