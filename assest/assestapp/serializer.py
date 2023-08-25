from rest_framework import serializers
from .models import Attandancetable,Employee
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import UserTable

class Attndanceseralizer(serializers.ModelSerializer):
    class Meta:
        model = Attandancetable
        fields ="__all__"

class Empserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user=UserTable.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        user = User(username=validated_data['username'], email=validated_data['email']) 
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        
        print(token.key)
        return user