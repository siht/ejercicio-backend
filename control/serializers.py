#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from django.contrib.auth.models import User
from rest_framework import serializers
from control import models as control_models

__all__ = ('ServiceSerializer','AreaSerializer', 'ItemSerializer', 'UserSerializer')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
        	'id',
        	#'password',
        	#'is_superuser',
        	#'username',
        	#'first_name',
        	#'last_name',
        	#'email',
        	#'is_active',
        	#'date_joined',
        	#'last_login'
    	)


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = control_models.Service
        fields = ('name', 'created_by', 'date_created', 'date_modified')


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer()
    service = ServiceSerializer()

    class Meta:
        model = control_models.Area
        fields = ('name', 'service', 'created_by', 'date_created', 'date_modified')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer()
    area = AreaSerializer()

    class Meta:
        model = control_models.Item
        fields = ('name', 'area', 'created_by', 'date_created', 'date_modified')
