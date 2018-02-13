#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the user model
"""
import pytest

from django.test import TestCase

from foodsharing_api.users.factories import UserFactory


class TestUser(TestCase):
    """Testing the User model"""

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

    def test_creation(self):
        """Test the creation of an user"""
        assert self.user.first_name == 'user'
        assert self.user.last_name == '1'
        assert self.user.is_active
        assert self.user.verified
        assert not self.user.is_staff
        for field in self.user._meta.local_fields:
            if field.name not in ['id', 'first_name', 'last_name','verified',
                                  'email', 'passwd', 'active']:
                assert not field.value_from_object(self.user)

    def test_password(self):
        """Testing password handling"""
        assert self.user.check_password(self.user.email)
        hashed_pwd = self.user.hash_password(self.user.email)
        assert hashed_pwd == self.user.passwd

        self.user.set_password('new_password')
        assert self.user.check_password('new_password')

