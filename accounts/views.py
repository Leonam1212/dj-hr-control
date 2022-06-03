from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .permissions import IsRH
from .serializers import AccountSerializer, LoginSerializer


class AccountView(generics.ListCreateAPIView):
    permission_classes = [IsRH]

    queryset = Account.objects
    serializer_class = AccountSerializer

class AccountUpdateAndDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]

    queryset = Account.objects
    serializer_class = AccountSerializer
    lookup_field = 'id'

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request: Request):
        try:
            token = LoginSerializer(data=request.data).authenticate()
            return Response({"token": token})
        except (ValidationError, AuthenticationFailed) as err:
            return Response(err.detail, err.status_code)
