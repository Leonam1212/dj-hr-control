from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsRH
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeView(generics.ListCreateAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateDestroyEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"
