# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
"""generic_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from control import api_urls as control_api_urls
from control import urls as control_urls

urlpatterns = [
    url(r'^$', include(control_urls, namespace='control', app_name='control')),
    url(r'^api/', include(control_api_urls, namespace='api-control', app_name='control')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    from general import views as general_views
    urlpatterns += [
        url(ur'^templates/(?P<template_name>.+)$', general_views.TemplateViewer.as_view(), name='template_testing')
    ]
else:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'general.views.view_404'
handler500 = 'general.views.view_500'
