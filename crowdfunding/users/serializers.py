from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)
class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.amount)
        instance.email = validated_data.get('email', instance.comment)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


