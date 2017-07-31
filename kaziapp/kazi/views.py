# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from models import Employer
from serializers import EmployerSerializer


class EmployersView(generics.ListCreateAPIView):
    """Add and view all employers."""

    model = Employer
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all
