from .models import ProjectService
from rest_framework import serializers

class ProjectServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectService
        fields = '__all__'