from urllib.parse import urlparse

from rest_framework import serializers
from rest_framework.validators import ValidationError

from config.settings import BASE_URL, PRIVATE


class CreateSerializer(serializers.Serializer):
    original = serializers.CharField(required=True)
    shortened = serializers.CharField(required=True)

    def validate_original(self, original):
        original_url = urlparse(original).netloc
        if PRIVATE and original_url != BASE_URL:
            raise ValidationError('Invalid Original URL')
        return original
