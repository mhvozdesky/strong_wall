from rest_framework import serializers
from .models import GreetingModel


class GreetingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = GreetingModel
        fields = ['name']
