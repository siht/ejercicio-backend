#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)
from django.contrib import admin
from control.models import *

admin.site.register(Service)
admin.site.register(Area)
admin.site.register(Item)
