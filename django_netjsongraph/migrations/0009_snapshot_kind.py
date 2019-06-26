# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsongraph', '0008_auto_20190416_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='kind',
            field=models.CharField(choices=[(b'normal', 'NORMAL'), (b'block_cut_tree', 'BLOCK_CUT_TREE')], db_index=True, default=(b'normal', 'NORMAL'), max_length=16, verbose_name='kind'),
        ),
    ]