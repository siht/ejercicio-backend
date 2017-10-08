# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from control import views as control_views

__all__ = ('urlpatterns',)

urlpatterns = [
    url(r'^$', control_views.index, name='index'),
]
