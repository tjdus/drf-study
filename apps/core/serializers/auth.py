from rest_framework import serializers

from apps.core.models import User


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("이미 가입된 이름입니다.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이미 가입된 이메일입니다.")
        return value


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid username or password.")

        return attrs
