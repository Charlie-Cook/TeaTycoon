# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(default='2016-01-19')),
                ('amount', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(default='2016-01-19')),
                ('amount', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='SupplyRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(default=None)),
                ('date', models.DateField(default='2016-01-19')),
                ('cost', models.FloatField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='member',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supply',
            name='stocked',
            field=models.BooleanField(default=False),
        ),
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
