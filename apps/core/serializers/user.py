from rest_framework import serializers

from apps.core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'is_active', 'is_staff']