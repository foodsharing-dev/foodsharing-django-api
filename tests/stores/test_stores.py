#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the store model
"""
from django.test import TestCase

from foodsharing_api.stores.factories import StoreFactory
from tests.utils import create_test_user_list
from tests.utils import create_test_conversation


class TestStore(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Setting up a test store"""
        cls.members = create_test_user_list()
        _, cls.conversation = create_test_conversation(cls.members)
        cls.store = StoreFactory.create(
            name='A Store',
            members=cls.members[1:],
            coordinators=[cls.members[0]],
            team_conversation=cls.conversation
        )

    def test_store_creation(self):
        """Test the creation of a store"""
        assert self.store.team.count() == 10
        assert self.store.team.get(storeteam__coordinator=1) == self.members[0]
