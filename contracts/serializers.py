from contracts.execptions import ShiftNotFoundError
from contracts.models import Contract
from shifts.serializers import ShiftScheduleSerializer, ShiftSerializer
from rest_framework import serializers
from shifts.models import Shift


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

        shift = serializers.CharField(max_length=20, write_only=True)

        extra_kwargs = {
            "id": {"read_only": True},
            "work_shift": {"required": False},
        }
    
    work_shift = ShiftSerializer()

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance: Contract, validated_data):
        request_data = self.context["request"].data

        if "shift" in request_data:
            shift_name = request_data.pop("shift")

            new_shift = Shift.objects.filter(name=shift_name)
            if not new_shift:
                raise ShiftNotFoundError
            instance.work_shift = new_shift.first()

        instance.contract_type = validated_data.get(
            "contract_type", instance.contract_type
        )
        instance.contract_duration = validated_data.get(
            "contract_duration", instance.contract_duration
        )
        instance.salary = validated_data.get("salary", instance.salary)
        instance.position = validated_data.get("position", instance.position)

        instance.save()
        return instance
        
class ContractScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["work_shift"]
        
    work_shift = ShiftScheduleSerializer()

    
