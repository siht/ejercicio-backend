# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render

__all__ = ('TemplateViewer',)

class TemplateViewer(TemplateView):
    def get(self, request, template_name):
        self.template_name = '{}.html'.format(template_name)
        return super(TemplateViewer, self).get(request)


def view_404(request):
    return render(request, '404.html', {})

def view_500(request):
    return render(request, '500.html', {})
