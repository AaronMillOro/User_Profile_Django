# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-07-21 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190721_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media/'),
        ),
    ]
