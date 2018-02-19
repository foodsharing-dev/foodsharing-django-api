#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the pickup models
"""
import datetime

from django.test import TestCase

from foodsharing_api.pickups.models import TakenPickup
from foodsharing_api.stores.factories import StoreFactory
from tests.utils import create_test_conversation
from tests.utils import create_test_pickups
from tests.utils import create_test_user_list


class TestPickups(TestCase):
    """Testing the Pickup model"""
    @classmethod
    def setUpTestData(cls):
        """Creating a test environment"""
        cls.members = create_test_user_list()
        _, cls.conversation = create_test_conversation(cls.members)
        cls.store = StoreFactory.create(
            name='A Store',
            members=cls.members[1:],
            coordinators=[cls.members[0]],
            team_conversation=cls.conversation
        )
        cls.pickups = create_test_pickups(cls.store, cls.members)

    def test_create_pickup(self):
        """Test creating of a Pickup"""
        for user in self.members:
            pickups = TakenPickup.objects.filter(user=user)
            assert len(pickups) == 1
