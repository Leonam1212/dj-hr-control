from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'email', 'name']

        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)
