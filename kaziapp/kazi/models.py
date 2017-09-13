# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employer(models.Model):
    """Define Employer attributes."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Define employee attributes."""

    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=True)
    employer = models.ForeignKey(Employer, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
