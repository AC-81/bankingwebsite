# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_balance',
            field=models.IntegerField(default=0),
        ),
    ]
