# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-25 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_tag_etc', '0002_auto_20181218_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='wallet12',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wallet_tag_etc.Wallet', verbose_name='Wallet12'),
        ),
    ]
