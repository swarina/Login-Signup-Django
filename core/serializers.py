from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=300, required=True)
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(max_length=300, required=True)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    first_name = serializers.CharField(max_length=300, required=True)
    last_name = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)
