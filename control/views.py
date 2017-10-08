#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from django.contrib.auth.models import User
from rest_framework import viewsets
from control import models as control_models
from control import serializers as control_serializers

__all__ = ('ServiceViewSet', 'AreaViewSet', 'ItemViewSet', 'UserViewSet')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = control_serializers.UserSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = control_models.Service.objects.filter(deleted=False)
    serializer_class = control_serializers.ServiceSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = control_models.Area.objects.filter(
        service__deleted=False,
        deleted=False
    )
    serializer_class = control_serializers.AreaSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = control_models.Item.objects.filter(
        area__service__deleted=False,
        area__deleted=False,
        deleted=False
    )
    serializer_class = control_serializers.ItemSerializer
