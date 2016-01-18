from django.db import models
import datetime as dt


class Member(models.Model):
    name = models.TextField(default=None)
    paid = models.BooleanField(default=False)


class Supply(models.Model):
    name = models.TextField(default=None)
    stocked = models.BooleanField(default=False)


class Collection(models.Model):
    date = models.DateField(default=dt.datetime.today().strftime('%Y-%m-%d'))
    amount = models.FloatField(default=None)


class Coffers(models.Model):
    date = models.DateField(default=dt.datetime.today().strftime('%Y-%m-%d'))
    amount = models.FloatField(default=None)


class SupplyRecord(models.Model):
    name = models.TextField(default=None)
    date = models.DateField(default=dt.datetime.today().strftime('%Y-%m-%d'))
    cost = models.FloatField(default=None)
