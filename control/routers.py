# -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from rest_framework import routers
from control import views as control_views

__all__ = ('router', )

router = routers.DefaultRouter()
router.register(r'users', control_views.UserViewSet)
router.register(r'services', control_views.ServiceViewSet)
router.register(r'areas', control_views.AreaViewSet)
router.register(r'items', control_views.ItemViewSet)