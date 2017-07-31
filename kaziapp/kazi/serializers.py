from rest_framework import serializers

from models import Employer, Employee


class EmployerSerializer(serializers.ModelSerializer):
    """Define JSON format of Employer."""

    class Meta:
        model = Employer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
