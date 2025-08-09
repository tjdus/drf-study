from rest_framework import serializers

from apps.core.models import ApplicationField
from apps.core.serializers.field import FieldSerializer


class ApplicationFieldSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)

    class Meta:
        model = ApplicationField
        fields = ['id', 'field']