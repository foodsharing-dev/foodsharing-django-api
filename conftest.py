#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration of pytest
"""

import pytest
from django.conf import settings

@pytest.fixture(scope='session')
def django_db_setup():
    """Using the exiting db"""
    settings.DATABASES['default']= {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodsharing',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '13306',
    }
