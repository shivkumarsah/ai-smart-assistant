# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-11 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciena', '0002_auto_20180911_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField()),
                ('solution', models.TextField()),
                ('confidence', models.CharField(max_length=5, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='tickets',
            old_name='subject',
            new_name='problem',
        ),
    ]
