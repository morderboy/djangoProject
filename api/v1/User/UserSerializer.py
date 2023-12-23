from rest_framework import serializers
from models import models
from models.models import Users


class CommentSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=32)
    email = serializers.EmailField()
    confirmed_email = serializers.BooleanField()

    def create(self, validated_data):
  	    return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.confirmed_email = validated_data.get('confirmed_email', instance.confirmed_email)
        instance.save()
        return instance