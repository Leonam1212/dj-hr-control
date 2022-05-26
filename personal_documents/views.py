from rest_framework import generics

from personal_documents.models import Personal_document
from personal_documents.serializers import PersonalDocumentSerializer

class PersonalDocumentsView(generics.ListCreateAPIView):
  queryset = Personal_document.objects.all()
  serializer_class = PersonalDocumentSerializer

class PersonalDocumentByIdView(generics.UpdateAPIView):
  queryset = Personal_document.objects.all()
  serializer_class = PersonalDocumentSerializer
  lookup_field = "id"