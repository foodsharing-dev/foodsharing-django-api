#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the conversation api
"""
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from tests.utils import create_test_user_list
from tests.utils import create_test_conversation


class TestConversationApi(APITestCase):
    """Test for the conversation app api"""

    @classmethod
    def setUpTestData(cls):
        """Creating test data"""
        cls.members = create_test_user_list()
        _, cls.conversation = create_test_conversation(cls.members)

    def test_getting_conversation_list_without_auth(self):
        """Testing the conversation list get api with authentication"""
        url = reverse('api/v1:conversation-list')
        response = self.client.get(url)
        assert response.status_code == 403

    def test_getting_conversation_list(self):
        """Test the conversation list get api"""
        url = reverse('api/v1:conversation-list')
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_getting_conversation_without_auth(self):
        """Testing the conversation get api with authentication"""
        url = reverse('api/v1:conversation-detail', kwargs={'pk':0})
        response = self.client.get(url)
        assert response.status_code == 403

    def test_getting_conversation(self):
        """Test the conversation get api"""
        url = reverse(
            'api/v1:conversation-detail',
            kwargs={'pk': self.conversation.pk}
        )
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200

