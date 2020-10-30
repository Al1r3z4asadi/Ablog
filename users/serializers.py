from djoser.serializers import UserCreateSerializer , UserSerializer 
from rest_framework import serializers as rest_serializer
from django.contrib.auth.models import User
from .models import Profile



class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id' , 'email' , 'username' , 'password' , 
                    'first_name' , 'last_name' )