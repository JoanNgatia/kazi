# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from models import Employer, Employee
# Create your tests here.
# test model creation


class ModelTestCase(TestCase):
    """Define correct model creation."""

    def setUp(self):
        """Add initial data."""
        self.name = 'J'
        self.new_employer = Employer(name=self.name)

    def test_new_model_creation(self):
        """Check new model instantiation."""
        initial_count = Employer.objects.count()
        # persist new data
        self.new_employer.save()
        new_count = Employer.objects.count()
        self.assertNotEqual(initial_count, new_count)

        self.name2 = 'employe223'
        self.new_employee = Employee(
            name=self.name2, employer=self.new_employer)
        self.new_employee.save()
        self.assertEqual(len(Employee.objects.all()), 1)


class ViewsTestCase(APITestCase):
    """Test Views to handle CRUD methods."""

    def setUp(self):
        """Add initial data."""
        self.client = APIClient()
        self.name = 'Employee1'
        self.name2 = 'Employer1'
        self.employer_data = {'name': self.name2}

    def test_new_employer_crud_methods(self):
        """Create, read, update test."""
        # test create
        self.response = self.client.post(
            reverse('all_employers'), self.employer_data, format='json')
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(len(Employer.objects.all()), 1)

        self.response = self.client.get(
            reverse('single_employer', kwargs={'pk': '1'}))
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('Employer1', self.response.data['name'])
