from contracts.models import Contract
from rest_framework import serializers

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True}
        }
