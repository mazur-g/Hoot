# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-02 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170902_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='img/default2.jpg', upload_to='img/'),
        ),
    ]
