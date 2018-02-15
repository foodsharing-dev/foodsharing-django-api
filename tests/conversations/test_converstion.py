#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the models of the conversation app
"""

from django.test import TestCase

from foodsharing_api.conversations.factories import ConversationFactory
from foodsharing_api.conversations.factories import ConversationMessageFactory
from foodsharing_api.users.factories import UserFactory



class TestConversation(TestCase):
    """Testing the conversation model"""

    @classmethod
    def setUpTestData(cls):
        """Setting a new conversation"""
        members = []
        for i in range(10):
            member = UserFactory.create(
                first_name='user',
                last_name=str(i),
                email='test{}@example.com'.format(i),
                geschlecht=0,
                newsletter=0
            )
            members.append(member)

        cls.conversation = ConversationFactory.create(
            name = 'twitter',
            members = members
        )
        cls.message = ConversationMessageFactory(
            body = u'Just a test message with german umlaute üäöß',
            sent_by = members[0],
            conversation=cls.conversation
        )

    def test_conversation(self):
        """Test the conversation creation"""
        assert self.conversation.name == 'twitter'
        assert self.conversation.members.count() == 10
        assert self.conversation.last_message == self.message
        assert self.message in self.conversation.messages.all()
