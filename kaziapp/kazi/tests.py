# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from models import Employer, Employee
# Create your tests here.
# test model creation


class ModelTestCase(TestCase):
    """Define correct model creation."""

    def setUp(self):
        self.name = 'J'
        self.name2 = 'employe223'
        self.new_employer = Employer(name=self.name)
        self.new_employee = Employee(name=self.name2, employer=self.new_employer)

    def test_new_model_creation(self):
        """Check new model instantiation."""
        initial_count = Employer.objects.count()
        # persist new data
        self.new_employer.save()
        new_count = Employer.objects.count()
        self.assertNotEqual(initial_count, new_count)
