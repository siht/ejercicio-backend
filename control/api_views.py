#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from control import models as control_models
from control import serializers as control_serializers

__all__ = ('ServiceViewSet', 'AreaViewSet', 'ItemViewSet', 'UserViewSet')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = control_serializers.UserSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = control_models.Service.objects.filter(deleted=False)
    serializer_class = control_serializers.ServiceSerializer

    def destroy(self, request, pk):
        instance = self.get_object()
        instance.deleted = True
        instance.deleted_by = request.user
        instance.save()
        areas_for_delete = instance.area_set.select_for_update().all()
        areas_for_delete.update(deleted=True, deleted_by=request.user)
        items_for_delete = (
            control_models.Item.objects
            .select_for_update()
            .filter(area__in=areas_for_delete)
        )
        items_for_delete.update(deleted=True, deleted_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AreaViewSet(viewsets.ModelViewSet):
    queryset = control_models.Area.objects.filter(
        service__deleted=False,
        deleted=False
    )
    serializer_class = control_serializers.AreaSerializer

    def destroy(self, request, pk):
        instance = self.get_object()
        instance.deleted = True
        instance.deleted_by = request.user
        instance.save()
        items_for_delete = instance.item_set.select_for_update().all()
        items_for_delete.update(deleted=True, deleted_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = control_models.Item.objects.filter(
        area__service__deleted=False,
        area__deleted=False,
        deleted=False
    )
    serializer_class = control_serializers.ItemSerializer

    def destroy(self, request, pk):
        instance = self.get_object()
        instance.deleted = True
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
