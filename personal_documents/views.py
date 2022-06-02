from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from employees.exceptions import EmployeeNotFoundError, ExistingPersonalDocumentsError

from employees.models import Employee
from .models import Personal_document
from .serializers import PersonalDocumentSerializer
from accounts.permissions import IsRH


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

            employee = Employee.objects.filter(id=employee_id)

            if not employee:
                raise EmployeeNotFoundError
            elif employee.first().personal_documents:
                raise ExistingPersonalDocumentsError

            new_personal_documents = serialized.save()
            employee.update(personal_documents=new_personal_documents)
            employee.first().save()

        except ValidationError:
            return Response({"detail": "Not found"}, status.HTTP_404_NOT_FOUND)

        return Response(serialized.data, status.HTTP_201_CREATED)


class ListPersonalDocumentsView(generics.ListAPIView):
    permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer
    lookup_field = "id"


class PersonalDocumentByIdView(generics.UpdateAPIView):
    permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer
    lookup_field = "id"
