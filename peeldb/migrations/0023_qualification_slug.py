# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0022_user_referer"),
    ]

    operations = [
        migrations.AddField(
            model_name="qualification",
            name="slug",
            field=models.SlugField(default="", max_length=500),
            preserve_default=False,
        ),
    ]