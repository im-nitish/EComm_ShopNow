# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userform', '0004_auto_20170421_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderplaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Address', models.TextField(max_length=200)),
                ('State', models.CharField(max_length=25)),
                ('PinCode', models.IntegerField()),
                ('Country', models.CharField(max_length=20)),
                ('Ordered_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
