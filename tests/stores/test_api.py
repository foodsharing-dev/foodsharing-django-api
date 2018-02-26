#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the store Api
"""
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from foodsharing_api.stores.factories import StoreFactory
from tests.utils import create_test_user_list
from tests.utils import create_test_conversation


class TestStoreApi(APITestCase):
    """Testing the store api"""


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

    def test_store_list_without_auth(self):
        """Testing list store api without authenticated user"""
        url = reverse('api/v1:store-list')
        response = self.client.get(url)
        assert response.status_code == 403

    def test_store_list(self):
        """Testing list store api with authenticated user"""
        url = reverse('api/v1:store-list')
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_store_detail_without_auth(self):
        """Testing store detail api without authenticated user"""
        url = reverse('api/v1:store-detail', kwargs={'pk': self.store.pk})
        response = self.client.get(url)
        assert response.status_code == 403

    def test_store_detail(self):
        """Testing store detail api with authenticated user"""
        url = reverse('api/v1:store-detail', kwargs={'pk': self.store.pk})
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_unknown_store(self):
        """Test with a unknown store id"""
        url = reverse('api/v1:store-detail', kwargs={'pk': 4711})
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 404

