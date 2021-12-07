# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-06 04:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0008_remove_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.AddField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='like', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]