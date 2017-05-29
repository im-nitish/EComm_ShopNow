# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userform', '0003_auto_20170421_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='PinCode',
            field=models.IntegerField(default=110062),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Address',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
