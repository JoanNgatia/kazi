from rest_framework import serializers

from models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    """Define JSON format of Employer."""

    class Meta:
        model = Employer
        fields = '__all__'
