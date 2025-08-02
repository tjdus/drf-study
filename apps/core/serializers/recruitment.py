from rest_framework import serializers

from apps.core.models import Recruitment
from apps.core.serializers.user import UserSerializer


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = ['title', 'content']

    def create(self, validated_data):
        recruitment = Recruitment.objects.create(**validated_data)
        return recruitment


class RecruitmentDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Recruitment
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'created_by']

