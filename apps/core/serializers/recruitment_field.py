from rest_framework import serializers

from apps.core.models import RecruitmentField
from apps.core.serializers.field import FieldSerializer


class RecruitmentFieldSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    class Meta:
        model = RecruitmentField
        fields = ['id', 'field', 'required_count']