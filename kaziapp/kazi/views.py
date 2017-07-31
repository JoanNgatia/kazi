# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from models import Employer
from serializers import EmployerSerializer


class EmployersView(generics.ListCreateAPIView):
    """Add and view all employers."""

    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployersDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View, update or delete single employer."""

    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
