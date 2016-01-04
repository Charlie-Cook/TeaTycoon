# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0002_auto_20160104_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
