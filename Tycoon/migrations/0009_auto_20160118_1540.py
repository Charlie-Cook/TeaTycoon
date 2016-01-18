# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0008_auto_20160106_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.TextField(default=None)),
                ('date', models.DateField(default='2016-01-18')),
                ('cost', models.FloatField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='coffers',
            name='date',
            field=models.DateField(default='2016-01-18'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date',
            field=models.DateField(default='2016-01-18'),
        ),
    ]
