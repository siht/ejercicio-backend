# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from control.routers import router

__all__ = ('urlpatterns',)

urlpatterns = [
    url(r'^', include(router.urls)),
]