#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the pickup api
"""
import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from foodsharing_api.stores.factories import StoreFactory
from tests.utils import create_test_pickups
from tests.utils import create_test_user
from tests.utils import create_test_conversation
from tests.utils import create_test_user_list


class TestPickUpApi(APITestCase):
    """Tests for the user app api"""

    @classmethod
    def setUpTestData(cls):
        """Creating a test environment"""
        cls.other_user = create_test_user()
        cls.members = create_test_user_list()
        _, cls.conversation = create_test_conversation(cls.members)
        cls.store = StoreFactory.create(
            name='A Store',
            members=cls.members[1:],
            coordinators=[cls.members[0]],
            team_conversation=cls.conversation
        )
        cls.pickups = create_test_pickups(cls.store, cls.members)

    def test_getting_pickups_without_auth(self):
        """Testing the pickup get api without authentication"""

        url = reverse(
            'pickup-detail',
            kwargs={'store': self.store.pk, 'at': self.pickups[0].at}
        )
        response = self.client.get(url)
        assert response.status_code == 403

    def test_getting_pickups_wrong_user(self):
        """Testing the pickup get api no member user"""

        url = reverse(
            'pickup-detail',
            kwargs={'store': self.store.pk, 'at': self.pickups[0].at}
        )
        self.client.login(username='test@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 403

    def test_getting_pickup(self):
        """Test the user get pickup"""
        url = reverse(
            'pickup-detail',
            kwargs={'store': self.store.pk, 'at': self.pickups[0].at}
        )
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200

