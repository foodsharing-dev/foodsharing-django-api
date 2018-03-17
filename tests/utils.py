#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Helper functions for the unit tests
"""
import datetime

from foodsharing_api.conversations.factories import ConversationMessageFactory
from foodsharing_api.conversations.factories import ConversationFactory
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

def create_test_user_list():
    """create a list of users"""
    members = []
    for i in range(10):
        member = UserFactory.create(
            first_name='user',
            last_name=str(i),
            email='test{}@example.com'.format(i),
            geschlecht=0,
            newsletter=0
        )
        member.set_password('password')
        members.append(member)
    return members

def create_test_conversation(members):
    """Creating a test conversation with anything necessary"""

    conversation = ConversationFactory.create(
        name = 'twitter',
        members = members
    )
    message = ConversationMessageFactory(
        body = u'Just a test message with german umlaute üäöß',
        sent_by = members[0],
        conversation=conversation
    )
    return message, conversation

def create_test_pickups(store, members):
    """Create a set of test pickups for a store"""
    from foodsharing_api.pickups.factories import TakenPickupFactory
    pickups = []
    for user in members:
        pickups.append(
            TakenPickupFactory.create(
                user=user,
                store=store,
                at=datetime.datetime.now() + datetime.timedelta(weeks=1)
            )
        )
    return pickups
