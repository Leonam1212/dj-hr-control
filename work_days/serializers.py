from rest_framework import serializers

from .models import WorkDay


class WorkDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDay
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return WorkDay.objects.create(**validated_data)

