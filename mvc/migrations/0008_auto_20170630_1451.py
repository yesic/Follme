# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-30 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0007_auto_20170630_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='logger',
            field=models.TextField(blank=True, default=b'', verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97'),
        ),
    ]
