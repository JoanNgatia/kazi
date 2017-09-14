# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from models import Employer, Employee
from serializers import EmployerSerializer, EmployeeSerializer


class EmployersView(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployeesView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
