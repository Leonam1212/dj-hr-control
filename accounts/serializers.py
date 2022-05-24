
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
class LoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()
