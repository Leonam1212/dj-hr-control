from rest_framework import generics
from contracts.models import Contract
from contracts.serializers import ContractSerializer
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsRH

class ContractView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsRH]
    
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class UpdateAndDeleteContractView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"
