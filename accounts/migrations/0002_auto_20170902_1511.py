# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-02 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample1.jpg', upload_to="{% static 'img/' %}"),
        ),
    ]
