from rest_framework import serializers

class ContractSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    contract_type = serializers.CharField()
    contract_duration = serializers.DateField()
    salary = serializers.FloatField()
    position = serializers.CharField()
    work_shift = serializers.CharField()