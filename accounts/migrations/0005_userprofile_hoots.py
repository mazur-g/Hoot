# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-08 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170902_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hoots',
            field=models.IntegerField(default=0),
        ),
    ]
