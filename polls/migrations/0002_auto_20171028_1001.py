# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-28 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ques_text',
            field=models.CharField(max_length=200, verbose_name='Question Text'),
        ),
    ]
