#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the user api
"""
from django.urls import reverse
from rest_framework.test import APITestCase

from foodsharing_api.users.factories import UserFactory


class TestUserApi(APITestCase):


    @classmethod
    def setUpTestData(cls):
        """Creating a test user"""
        cls.user = UserFactory.create(
            first_name='user',
            last_name='1',
            email='test@example.com',
            geschlecht=0,
            newsletter=0
        )
        cls.user.set_password('password')

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
