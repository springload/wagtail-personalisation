# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0013_auto_20170606_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmentvisit',
            name='session',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
