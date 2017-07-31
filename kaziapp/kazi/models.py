# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employer(models.Model):
    """Define Employer attributes."""

    name = models.CharField(max_length=255, blank=False)


class Employee(models.Model):
    """Define employee attributes."""

    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
