from contracts.models import Contract
from shifts.serializers import ShiftScheduleSerializer, ShiftSerializer
from rest_framework import serializers

class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True}
        }
    
    work_shift = ShiftSerializer()

    def create(self, validated_data):
        return super().create(validated_data)
        
class ContractScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["work_shift"]
        
    work_shift = ShiftScheduleSerializer()
