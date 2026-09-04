from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    password = serializers.CharField()

class UserAuthSerializer(UserBaseSerializer):
    pass 

class UserCreateSerializer(UserBaseSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')

class VerifyCodeValid(serializers.Serializer):
    username = serializers.CharField(max_length = 25)
    code = serializers.IntegerField(min_value=100000,max_value=999999)
