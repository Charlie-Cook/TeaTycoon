# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0005_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='amount',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='collection',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
