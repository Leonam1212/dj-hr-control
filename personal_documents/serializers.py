from rest_framework import serializers

from personal_documents.models import Personal_document


class PersonalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_document
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return Personal_document.objects.create(**validated_data)
