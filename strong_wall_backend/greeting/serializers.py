import requests
from rest_framework import serializers
from django.conf import settings
from .models import GreetingModel


class GreetingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    captcha = serializers.CharField(required=True)

    class Meta:
        model = GreetingModel
        fields = ['name', 'captcha']

    def validate_captcha(self, value):
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': value
        }
        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if not result.get('success'):
            raise serializers.ValidationError(
                'Invalid reCAPTCHA. Please try again.')

        return value
