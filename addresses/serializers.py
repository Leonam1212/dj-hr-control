from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
