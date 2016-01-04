from django.db import models


class Member(models.Model):
    name = models.TextField(default=None)
    paid = models.BooleanField(default=False)


class Supply(models.Model):
    name = models.TextField(default=None)
