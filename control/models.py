#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

__all__ = ('Service', 'Area', 'Item')

@python_2_unicode_compatible
class Service(models.Model):
    name = models.CharField(max_length=64)
    created_by = models.ForeignKey('auth.User', related_name='service_created_by')
    deleted_by = models.ForeignKey('auth.User', related_name='service_deleted_by', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


@python_2_unicode_compatible
class Area(models.Model):
    name = models.CharField(max_length=64)
    service = models.ForeignKey('Service')
    created_by = models.ForeignKey('auth.User', related_name='area_created_by')
    deleted_by = models.ForeignKey('auth.User', related_name='area_deleted_by', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


@python_2_unicode_compatible
class Item(models.Model):
    name = models.CharField(max_length=64)
    area = models.ForeignKey('Area')
    created_by = models.ForeignKey('auth.User', related_name='item_created_by')
    deleted_by = models.ForeignKey('auth.User', related_name='item_deleted_by', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)
