# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo', '0006_auto_20170711_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='algo',
            name='params',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
