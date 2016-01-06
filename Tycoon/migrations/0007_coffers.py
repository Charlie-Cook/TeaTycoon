# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0006_auto_20160106_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffers',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(default=None)),
                ('amount', models.FloatField(default=None)),
            ],
        ),
    ]
