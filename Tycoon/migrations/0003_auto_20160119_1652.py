# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0002_auto_20160119_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.TextField(default=None, null=True),
        ),
    ]
