# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-23 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20171216_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltask',
            name='project',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Project'),
        ),
    ]