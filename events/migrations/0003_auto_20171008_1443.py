# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_participantes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participantes',
            new_name='Participante',
        ),
    ]
