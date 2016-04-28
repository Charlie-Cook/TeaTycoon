from django.db import models
import datetime as dt


class Member(models.Model):
    name = models.TextField(default=None)
    paid = models.BooleanField(default=False)
    email = models.TextField(default=None, null=True)

    class Meta:
        verbose_name_plural = 'Members'


class Supply(models.Model):
    name = models.TextField(default=None)
    stocked = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Supplies'


class Collection(models.Model):
    date = models.DateField(default=dt.datetime.today().strftime('%Y-%m-%d'))
    amount = models.FloatField(default=None)

    class Meta:
        verbose_name_plural = 'Collections'


class Coffers(models.Model):
    date = models.DateField(default=dt.datetime.today().strftime('%Y-%m-%d'))
    amount = models.FloatField(default=None)

    class Meta:
        verbose_name_plural = 'Coffers'


class SupplyRecord(models.Model):
    name = models.TextField(default=None)
    date = models.DateField(default=dt.datetime.today().strftime('%Y-%m-%d'))
    cost = models.FloatField(default=None)

    class Meta:
        verbose_name_plural = 'Supply Records'
