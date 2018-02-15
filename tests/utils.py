#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Helper functions for the unit tests
"""
from foodsharing_api.users.factories import UserFactory


def create_test_user():
    """Creating a test user"""
    user = UserFactory.create(
        first_name='user',
        last_name='1',
        email='test@example.com',
        geschlecht=0,
        newsletter=0
    )
    user.set_password('password')
    return user
