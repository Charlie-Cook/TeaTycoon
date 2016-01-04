from django.db import models


class Member(models.Model):
    name = models.TextField(default=None)


class Supply(models.Model):
    name = models.TextField(default=None)
