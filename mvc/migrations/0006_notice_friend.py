# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0005_notice_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x98\x85\xe8\xaf\xbb')),
                ('type', models.IntegerField(verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_friend_receiver', to='mvc.User', verbose_name=b'\xe6\x8e\xa5\xe5\x8f\x97\xe8\x80\x85')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_friend_sender', to='mvc.User', verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe8\x80\x85')),
            ],
            options={
                'ordering': ['-create_date'],
                'verbose_name_plural': '\u6dfb\u52a0\u597d\u53cb\u901a\u77e5',
            },
        ),
    ]
