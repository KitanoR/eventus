# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20171008_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
