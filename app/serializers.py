from rest_framework import serializers
from rest_framework.validators import ValidationError

from config.settings import BASE_URL


class CreateSerializer(serializers.Serializer):
    original = serializers.CharField(required=True)
    shortened = serializers.CharField(required=True)

    def validate_original(self, original):
        # TODO: Make it configurable
        if not original.startswith(BASE_URL):
            raise ValidationError('Invalid Original URL')
        return original
