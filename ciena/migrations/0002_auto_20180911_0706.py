# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-11 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciena', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
