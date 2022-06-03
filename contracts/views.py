from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.permissions import IsRH
from employees.exceptions import EmployeeNotFoundError, ExistingContractError
from employees.models import Employee

from .models import Contract
from .serializers import ContractSerializer


class CreateContractView(generics.CreateAPIView, generics.RetrieveAPIView):
    permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def post(self, request: Request, employee_id=""):
        try:
            serialized: ContractSerializer = self.get_serializer(data=request.data)
            serialized.is_valid(True)

            employee = Employee.objects.filter(id=employee_id)

            if not employee:
                raise EmployeeNotFoundError
            elif employee.first().contract:
                raise ExistingContractError

            new_contract = serialized.save()
            employee.update(contract=new_contract)
            employee.first().save()

        except ValidationError:
            return Response({"detail": "Not found"}, status.HTTP_400_BAD_REQUEST)

        return Response(serialized.data, status.HTTP_201_CREATED)


class ListContractView(generics.ListAPIView):
    permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"


class UpdateAndDeleteContractView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"
