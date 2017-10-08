#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

__all__ = ('index',)

@login_required
@require_GET
def index(request):
    return render(request, 'control/index.html', {})
