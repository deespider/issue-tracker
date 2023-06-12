from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from projects.models import Project

class ProjectAddSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=50)
    project_description = serializers.CharField(max_length=200, required=False, allow_null=True, allow_blank=True)
    project_link = serializers.URLField(required=False, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)