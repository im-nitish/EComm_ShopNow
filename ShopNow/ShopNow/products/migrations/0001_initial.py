# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-16 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('A', models.IntegerField(null=True)),
                ('B', models.IntegerField(null=True)),
                ('C', models.IntegerField(null=True)),
                ('D', models.IntegerField(null=True)),
                ('image', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
