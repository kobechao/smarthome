# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_rpi_test_data_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpi_test_data',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
