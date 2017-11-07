# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RPi_Test_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('rPin', models.CharField(max_length=20)),
                ('gPin', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
