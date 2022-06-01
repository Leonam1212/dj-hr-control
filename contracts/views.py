from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from employees.models import Employee
from shifts.models import Shift
from .models import Contract
from .execptions import ShiftNotFoundError
from .serializers import ContractSerializer
from accounts.permissions import IsRH


class CreateContractView(generics.GenericAPIView):
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def post(self, request: Request, employee_id=""):
        try:
            serialized: ContractSerializer = self.get_serializer(data=request.data)
            serialized.is_valid(True)
            shift_name: str = request.data.pop("shift").lower().strip()

            work_shift = Shift.objects.filter(name=shift_name)

            if not work_shift:
                raise ShiftNotFoundError

            serialized.validated_data["work_shift"] = work_shift.first()

            employee = Employee.objects.filter(pk=employee_id)

            if not employee:
                raise ObjectDoesNotExist

            if employee.first().contract:
                return Response(
                    {"detail": "Employee already has a contract"},
                    status.HTTP_409_CONFLICT,
                )

            new_contract = serialized.save()

            employee.update(contract=new_contract)
            employee.first().save()

            return Response(serialized.data, status.HTTP_201_CREATED)

        except (ValidationError, ObjectDoesNotExist):
            return Response({"detail": "Not found"}, status.HTTP_404_NOT_FOUND)


class ListContractView(generics.ListAPIView):
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"


class UpdateAndDeleteContractView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"

