# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releaserecorder', '0003_releaseapplication_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='releaseapplication',
            old_name='application_description',
            new_name='application_note',
        ),
    ]