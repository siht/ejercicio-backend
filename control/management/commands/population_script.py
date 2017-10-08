#! -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import csv
import logging
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User
from control import models as control_models

class Command(BaseCommand):
    help = 'first populate of models'
    full_file_path = os.path.join(
        settings.BASE_DIR,
        'control',
        'management',
        'commands',
        'Catalogo de Servicios.csv'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--file',
            dest='set_file',
            help='choose a file instead of initial file'
        )

    def handle(self, *args, **options):
        if options['set_file']:
            self.full_file_path = options['set_file']
        admin = User.objects.get(id=1)
        with open(self.full_file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=b',')
            reader.next()
            for row in reader:
                service, _ = control_models.Service.objects.get_or_create(name=row[0], created_by=admin)
                if _:
                    print('servicio creado')
                area, _ = control_models.Area.objects.get_or_create(name=row[1], created_by=admin, service=service)
                if _:
                    print('area creada')
                item = control_models.Item.objects.create(name=row[2], created_by=admin, area=area)
