from django.db import models


class Member(models.Model):
    name = models.TextField(default=None)
    paid = models.BooleanField(default=False)


class Supply(models.Model):
    name = models.TextField(default=None)
    stocked = models.BooleanField(default=False)


class Collection(models.Model):
    date = models.DateField(default=None)
    amount = models.FloatField(default=None)


class Coffers(models.Model):
    date = models.DateField(default=None)
    amount = models.FloatField(default=None)
