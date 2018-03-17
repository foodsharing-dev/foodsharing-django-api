"""foodsharing_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from foodsharing_api.conversations.api import ConversationViewSet
from foodsharing_api.pickups.api import PickupViewSet
from foodsharing_api.session.api import SessionViewSet
from foodsharing_api.stores.api import StoreViewSet
from foodsharing_api.users.api import UserViewSet


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'pickups', PickupViewSet)

pickup_detail = PickupViewSet.as_view({'get':'retrieve'})
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include((router.urls, 'api/v1'))),
    url(r'^api/v1/session/', SessionViewSet.as_view({'get': 'status', 'post': 'login', 'delete': 'logout'})),
    url(r'^api/v1/pickups/(?P<store>\d+)/(?P<at>[^/]+)/$', pickup_detail, name='pickup-detail'),
    url(r'^docs/', get_swagger_view()),
    url(r'^silk/', include(('silk.urls', 'silk'))),
]
