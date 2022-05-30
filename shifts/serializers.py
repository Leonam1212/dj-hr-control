from rest_framework import serializers

from shifts.models import Shift

class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
        