from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .permissions import IsRH
from .models import Account
from .serializers import LoginSerializer,AccountSerializer

    
class AccountView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsRH]
    queryset = Account.objects
    serializer_class = AccountSerializer
    
    def create(self, request: Request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = Account.objects.create(**serializer.validated_data)
        user.set_password(serializer.validated_data["password"])           
        user.save()

        serializer = AccountSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginView(APIView):

    def post(self, request: Request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )

        if not user:
            return Response({"message": "Invalid Credentials"}, status.HTTP_401_UNAUTHORIZED)
        
        token,_ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})
