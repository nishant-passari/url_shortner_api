from rest_framework import serializers
from rest_framework.fields import URLField

class ShortnerSerializer(serializers.Serializer):
    url = URLField(max_length=200, allow_blank=False)