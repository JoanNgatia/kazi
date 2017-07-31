# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from models import Employer, Employee
from serializers import EmployerSerializer, EmployeeSerializer


class EmployersView(generics.ListCreateAPIView):
    """Add and view all employers."""

    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployersDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View, update or delete single employer."""

    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployeesView(generics.ListCreateAPIView):
    """Add and view all employees."""

    serializer_class = EmployeeSerializer

    def get_queryset(self):
        pk = self.kwargs.get('employer_id')
        return Employee.objects.filter(employer=pk)
