from rest_framework import serializers

from .models import Shift


class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True}
        }

    def validate(self, attrs):
        attrs["name"] = attrs["name"].lower().strip()

        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
        
# class ShiftScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shift
#         fields = ["name", "base_checkin", "base_checkout"]


