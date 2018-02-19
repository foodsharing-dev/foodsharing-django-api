import datetime

from django.core.management import BaseCommand

from foodsharing_api.conversations.factories import ConversationFactory, ConversationMessageFactory
from foodsharing_api.pickups.factories import TakenPickupFactory
from foodsharing_api.stores.factories import StoreFactory
from foodsharing_api.stores.models import Store as StoreModel
from foodsharing_api.users.factories import UserFactory
from foodsharing_api.users.models import User as UserModel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--reset-sample-data', action='store_true', dest='reset_sample_data')

    def handle(self, *args, **options):
        def print(*args):
            self.stdout.write(' '.join([str(_) for _ in args]))

        def print_success(*args):
            self.stdout.write(self.style.SUCCESS(' '.join(str(_) for _ in args)))

        if options['reset_sample_data']:
            UserModel.objects.all().delete()
            StoreModel.objects.all().delete()

        u1 = UserFactory.create(first_name='user', last_name='1', email='user1@example.com')
        u2 = UserFactory.create(first_name='user', last_name='2', email='user2@example.com')
        ub = UserFactory.create(first_name='user', last_name='Bot', email='userBot@example.com')

        convs1 = ConversationFactory.create(members=[u1, u2, ub], locked=True)
        convs2 = ConversationFactory.create(members=[u2], locked=True)
        s1 = StoreFactory.create(name='A Store', members=[u1, u2], coordinators=[ub], team_conversation=convs1)
        s2 = StoreFactory.create(name='B Store', coordinators=[u2], team_conversation=convs2)

        conv1 = ConversationFactory.create(members=[u1, u2, ub])
        conv2 = ConversationFactory.create(members=[u1, u2])
        ConversationFactory.create(members=[u2, ub])


        ConversationMessageFactory(conversation=conv1, sent_by=u2, sent_at=datetime.datetime.now() - datetime.timedelta(days=1))
        ConversationMessageFactory(conversation=conv1, sent_by=u1)
        ConversationMessageFactory(conversation=conv2, sent_by=u1)

        TakenPickupFactory.create(user=u1, store=s1, at=datetime.datetime.now() + datetime.timedelta(weeks=1))
        TakenPickupFactory.create(user=u2, store=s1, at=datetime.datetime.now() + datetime.timedelta(weeks=1))
        TakenPickupFactory.create(user=u1, store=s1, at=datetime.datetime.now() + datetime.timedelta(weeks=1, days=1))
        TakenPickupFactory.create(user=u2, store=s2, at=datetime.datetime.now() + datetime.timedelta(weeks=1))
