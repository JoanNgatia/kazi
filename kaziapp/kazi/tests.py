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
        self.employer = Employer.objects.create(name='Andela')
        self.new_employer_data = {'name': self.name2}
        self.employee = Employee.objects.create(
            name='Employee1', email='jngatia@abc.com', employer=self.employer)

    def test_new_employer_crud_methods(self):
        """Create, read, update test."""
        # test create
        self.response = self.client.post(
            reverse('all_employers'), self.new_employer_data, format='json')
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(len(Employer.objects.all()), 2)

        # test one employer retrieve
        self.response = self.client.get(
            reverse('single_employer', kwargs={'pk': '1'}))
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('Andela', self.response.data['name'])

        # test one employer update
        self.response = self.client.put(reverse('single_employer', kwargs={
                                        'pk': '1'}), {'name': 'New Employer'})
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('New Employer', self.response.data['name'])

    def test_new_employee_crud_methods(self):
        """Create read update delete employees."""
        self.response = self.client.get(
            reverse('all_employees', kwargs={'employer_id': self.employee.id}))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(len(Employee.objects.all()), 1)

        self.response = self.client.post(
            reverse('all_employees', kwargs={'employer_id': self.employer.id}),
            {'name': 'Ashley!'})
        # self.assertEqual(response.status_code, 201)
        self.assertEqual(Employee.objects.count(), 2)

    #     # unsuccessful item creation
    #     response = self.client.post(
    #         reverse('bucketlistitems_get', kwargs={'pk': self.bucketlist.id}),
    #         {'name': ''})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Bucketlistitem.objects.count(), 6)

    # def test_edition_of_bucketlistitems(self):
    #     """Test that a user can change the name of a bucketlist item."""
    #     response = self.client.post(
    #         reverse('bucketlistitems_update',
    #                 kwargs={'pk': self.bucketlistitem.id,
    #                         'bucketlist': self.bucketlist.id}),
    #         {'name': 'MAdtraxx!!'})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Bucketlistitem.objects.count(), 5)
    #     self.assertEqual(
    #         Bucketlistitem.objects.get(id=self.bucketlistitem.id).name,
    #         'MAdtraxx!!')

