from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from contracts.models import Contract

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT
)

from contracts.serializers import ContractSerializer

class ContractView(APIView):
    def get(self, request: Request ):
        contracts =  Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        print(serializer.data)

        return Response(serializer.data, HTTP_200_OK)

    def post(self,  request: Request):
        serializer = ContractSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contract = Contract.objects.create(**serializer.validated_data)
        contract.save()

        serializer = ContractSerializer(contract)

        return Response(serializer.data, HTTP_201_CREATED)
    
    def put(self, request: Request):
        ...

    def delete(self, request: Request, contract_id=""):
       
            if contract_id:
                contract = Contract.objects.filter(pk = contract_id)

                if not contract.exists():
                    return Response({"message": "Contract does not exist"}, HTTP_404_NOT_FOUND)
            

                contract.first().delete()

                return Response("", HTTP_204_NO_CONTENT)

            return Response({"message": "Submit a contract id"}, HTTP_404_NOT_FOUND)
     