from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from employees.models import Employee
from .models import Personal_document
from .serializers import PersonalDocumentSerializer
from accounts.permissions import IsRH


class CreatePersonalDocumentsView(generics.GenericAPIView):
    # permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer

    def post(self, request: Request, employee_id=""):
        try:
            serialized: PersonalDocumentSerializer = self.get_serializer(
                data=request.data
            )
            serialized.is_valid(True)

            employee = Employee.objects.filter(pk=employee_id)

            if not employee:
                raise ObjectDoesNotExist

            if employee.first().personal_documents:
                return Response(
                    {
                        "detail": "Employee already has his personal documents registered"
                    },
                    status.HTTP_409_CONFLICT,
                )

            new_personal_documents = serialized.save()

            employee.update(personal_documents=new_personal_documents)
            employee.first().save()

            return Response(serialized.data, status.HTTP_201_CREATED)

        except (ValidationError, ObjectDoesNotExist):
            return Response({"detail": "Not found"}, status.HTTP_404_NOT_FOUND)


class ListPersonalDocumentsView(generics.ListAPIView):
    # permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer
    lookup_field = "id"

class PersonalDocumentByIdView(generics.UpdateAPIView):
    # permission_classes = [IsRH]

    queryset = Personal_document.objects.all()
    serializer_class = PersonalDocumentSerializer
    lookup_field = "id"
