from .models import UserService
from rest_framework import serializers

class UserServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserService
        fields = '__all__'