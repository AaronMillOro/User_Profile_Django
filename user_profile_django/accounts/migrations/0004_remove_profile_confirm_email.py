# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-07-22 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190722_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='confirm_email',
        ),
    ]
