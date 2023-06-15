# users/serializers.py
from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    designation = serializers.CharField(max_length=60, required=False, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        user = CustomUser.objects.create(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
