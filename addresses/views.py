from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from employees.models import Employee
from .models import Address
from .serializers import AddressSerializer
from accounts.permissions import IsRH


class CreateAddressView(generics.GenericAPIView):
    # permission_classes = [IsRH]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def post(self, request: Request, employee_id=""):
        try:
            serialized: AddressSerializer = self.get_serializer(data=request.data)
            serialized.is_valid(True)

            employee = Employee.objects.filter(pk=employee_id)

            if not employee:
                raise ObjectDoesNotExist

            if employee.first().address:
                return Response(
                    {"detail": "Employee already has an address"},
                    status.HTTP_409_CONFLICT,
                )

            new_address = serialized.save()

            employee.update(address=new_address)
            employee.first().save()

            return Response(serialized.data, status.HTTP_201_CREATED)

        except (ValidationError, ObjectDoesNotExist):
            return Response({"detail": "Not found"}, status.HTTP_404_NOT_FOUND)


class ListAddressView(generics.ListAPIView):
    # permission_classes = [IsRH]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"


class UpdateDestroyAddressView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"
