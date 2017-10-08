# -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from rest_framework import routers
from control import api_views as control_api_views

__all__ = ('router', )

router = routers.DefaultRouter()
router.register(r'users', control_api_views.UserViewSet)
router.register(r'services', control_api_views.ServiceViewSet)
router.register(r'areas', control_api_views.AreaViewSet)
router.register(r'items', control_api_views.ItemViewSet)
