from rest_framework import generics
from accounts.permissions import IsRH
from .models import Employee
from .serializers import EmployeeDetailedSerializer, EmployeeSerializer


class EmployeeView(generics.ListCreateAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeDetailedSerializer
        return super().get_serializer_class()

class UpdateDestroyEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"
