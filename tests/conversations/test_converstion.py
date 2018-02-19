#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the models of the conversation app
"""

from django.test import TestCase

from tests.utils import create_test_conversation
from tests.utils import create_test_user_list


class TestConversation(TestCase):
    """Testing the conversation model"""

    @classmethod
    def setUpTestData(cls):
        """Setting a new conversation"""
        members = create_test_user_list()
        cls.message, cls.conversation = create_test_conversation(members)
    def test_conversation(self):
        """Test the conversation creation"""
        assert self.conversation.name == 'twitter'
        assert self.conversation.members.count() == 10
        assert self.conversation.last_message == self.message
        assert self.message in self.conversation.messages.all()
