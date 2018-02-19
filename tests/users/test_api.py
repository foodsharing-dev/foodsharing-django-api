#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the user api
"""
from django.urls import reverse
from rest_framework.test import APITestCase

from tests.utils import create_test_user


class TestUserApi(APITestCase):
    """Tests for the user app api"""

    @classmethod
    def setUpTestData(cls):
        """Creating a test user"""
        cls.user = create_test_user()

    def test_getting_user_without_auth(self):
        """Testing the user get api with authentication"""

        url = reverse('api/v1:user-detail', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        assert response.status_code == 403

    def test_getting_user(self):
        """Test the user get api"""
        url = reverse('api/v1:user-detail', kwargs={'pk': self.user.id})
        self.client.login(username='test@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200
