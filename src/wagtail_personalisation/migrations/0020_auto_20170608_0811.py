# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0019_auto_20170608_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segmentvisit',
            name='segment',
        ),
        migrations.AddField(
            model_name='segmentvisit',
            name='segments',
            field=models.ManyToManyField(to='wagtail_personalisation.Segment'),
        ),
    ]
