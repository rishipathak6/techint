# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-01 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180928_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='tagline',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
