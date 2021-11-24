from rest_framework import serializers
from user.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=256, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=32)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name']

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance
