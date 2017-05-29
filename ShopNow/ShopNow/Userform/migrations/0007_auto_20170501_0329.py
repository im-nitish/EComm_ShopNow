# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Userform', '0006_auto_20170421_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Ordered_on',
        ),
        migrations.AddField(
            model_name='order',
            name='Name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
