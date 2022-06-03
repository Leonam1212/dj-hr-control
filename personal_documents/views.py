from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.permissions import IsRH
from contracts.models import Contract
from contracts.serializers import ContractSerializer
from employees.exceptions import (EmployeeNotFoundError,
                                  ExistingPersonalDocumentsError)
from employees.models import Employee

from .models import Personal_document
from .serializers import PersonalDocumentSerializer


class CreatePersonalDocumentsView(generics.GenericAPIView):
    permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer

    def post(self, request: Request, employee_id=""):
        try:
            serialized: PersonalDocumentSerializer = self.get_serializer(
                data=request.data
            )
            serialized.is_valid(True)

            employee = Employee.objects.filter(id=employee_id).first()

            if not employee:
                raise EmployeeNotFoundError
            elif employee.personal_documents:
                raise ExistingPersonalDocumentsError

            if (employee.contract and not serialized.data["cnpj"]):
                contract: Contract = ContractSerializer(employee.contract).data
                contract_type: str = contract["contract_type"]

                if (contract_type.upper() == "PJ"):
                    return Response({
                            "detail": "cnpj is required because this employee contract is PJ"
                        }, status.HTTP_400_BAD_REQUEST )

            new_personal_documents = Personal_document.objects.create(**serialized.validated_data)
            employee.personal_documents = new_personal_documents
            employee.save()

            return Response(serialized.validated_data, status.HTTP_201_CREATED)

        except ValidationError:
            return Response({"detail": "Not found"}, status.HTTP_404_NOT_FOUND)



class ListPersonalDocumentsView(generics.ListAPIView):
    permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer
    lookup_field = "id"


class PersonalDocumentByIdView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer
    lookup_field = "id"
