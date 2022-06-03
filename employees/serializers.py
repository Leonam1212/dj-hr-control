from rest_framework import serializers

from .models import Employee

# from addresses.serializers import AddressSerializer
# from contracts.serializers import ContractSerializer
# from personal_documents.serializers import PersonalDocumentSerializer



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
            "contract": {"required": False},
            "personal_documents": {"required": False},
            "address": {"required": False},
        }

    def validate(self, attrs):
        attrs["name"] = attrs["name"].title().strip()
        return super().validate(attrs)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

# class EmployeeDetailedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['id', 'name', 'email', 'phone_number', "personal_code", 'contract', 'personal_documents', 'address']
    
#     contract = ContractSerializer()
#     personal_documents = PersonalDocumentSerializer()
#     # address = AddressSerializer()


# class EmployeeScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ["name", "contract"]
    
#     contract = ContractScheduleSerializer()