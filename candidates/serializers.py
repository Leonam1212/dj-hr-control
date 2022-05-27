from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
            "pdf_file": {"write_only": True}
        }

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)
