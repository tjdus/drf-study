from rest_framework import serializers

from apps.core.models import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'name']