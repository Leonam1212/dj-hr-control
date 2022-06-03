from django.contrib.auth import authenticate, hashers
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}        

    def create(self, validated_data):

        validated_data["password"] = hashers.make_password(validated_data.get("password"))
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = hashers.make_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()

    def authenticate(self):
        self.is_valid(True)

        user = authenticate(**self.data)
        if not user:
            raise AuthenticationFailed()
        
        token,_ = Token.objects.get_or_create(user=user)

        return token.key
