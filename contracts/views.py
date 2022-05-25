from rest_framework import generics
from contracts.models import Contract
from contracts.serializers import ContractSerializer

class ContractView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class UpdateAndDeleteContractView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"
