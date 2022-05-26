from rest_framework import serializers

from personal_documents.models import Personal_document

class PersonalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_document
        fields = "__all__"