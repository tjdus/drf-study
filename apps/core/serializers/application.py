from rest_framework import serializers

from apps.core.models import Application, ApplicationField, Field
from apps.core.serializers.application_field import ApplicationFieldSerializer
from apps.core.serializers.user import UserSerializer

# 생성/수정용
class ApplicationSerializer(serializers.ModelSerializer):
    fields = serializers.ListField(
        child=serializers.IntegerField()
    )
    class Meta:
        model = Application
        fields = ['recruitment', 'content', 'fields']

    def validate_fields(self, value):
        for field in value:
            if not Field.objects.get(id=field):
                raise serializers.ValidationError(f"Field with id {field} does not exist.")
        return value

    def create(self, validated_data):
        fields_data = validated_data.pop('fields', None)
        application = Application.objects.create(**validated_data)

        for field_id in fields_data:
            ApplicationField.objects.create(
                application=application,
                field_id=field_id
            )

        return application

# 조회용
class ApplicationDetailSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    fields = ApplicationFieldSerializer(many=True, read_only=True, source="application_field_set")

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'recruitment', 'content', 'fields']
