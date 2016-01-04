# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0003_member_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='stocked',
            field=models.BooleanField(default=False),
        ),
    ]
