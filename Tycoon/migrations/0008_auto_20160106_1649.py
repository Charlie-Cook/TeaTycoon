# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0007_coffers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffers',
            name='date',
            field=models.DateField(default='2016-01-06'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date',
            field=models.DateField(default='2016-01-06'),
        ),
    ]
