# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userform', '0005_orderplaced'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userdata',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Orderplaced',
            new_name='Order',
        ),
    ]