# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20171030_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userid',
        ),
        migrations.AddField(
            model_name='profile',
            name='account_number',
            field=models.IntegerField(default=0),
        ),
    ]
