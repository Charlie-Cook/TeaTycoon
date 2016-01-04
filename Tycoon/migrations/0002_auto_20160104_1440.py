# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='supply',
            name='name',
            field=models.TextField(default=None),
        ),
    ]
