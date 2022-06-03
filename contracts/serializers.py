from rest_framework import serializers

from contracts.models import Contract
from shifts.exceptions import ShiftNotFoundError
from shifts.models import Shift
from shifts.serializers import ShiftSerializer

from .exceptions import ShiftNotSentError


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        work_shift = ShiftSerializer()

        extra_kwargs = {"id": {"read_only": True}, "work_shift": {"required": False}}


    def create(self, validated_data):
        request_data = self.context["request"].data

        if "shift" in request_data:
            shift_name: str = request_data.pop("shift").lower().strip()
        else:
            raise ShiftNotSentError

        work_shift = Shift.objects.filter(name=shift_name).first()

        if not work_shift:
            raise ShiftNotFoundError

        return Contract.objects.create(**validated_data, work_shift=work_shift)


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
