# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_auto_20170716_0315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjecttag',
            old_name='subject',
            new_name='label',
        ),
    ]
