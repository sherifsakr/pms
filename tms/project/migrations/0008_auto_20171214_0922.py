# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20171214_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
