from django.shortcuts import render
from .models import Market, Contract

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContractSerializer

@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/contracts/',
        'Detail': '/contract-detail/<str:pk>/',
        'Create': '/contract-create/',
        'Update': '/contract-update/<str:pk>/',
        'Delete': '/contract-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def showContracts(request):
    contracts = Contract.objects.all()
    serializer = ContractSerializer(contracts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def detailContract(request, pk):
    contract = Contract.objects.get(id=pk)
    serializer = ContractSerializer(contract, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def createContract(request):
    serializer = ContractSerializer(request.data)

    if serializer.is_valid():
        serializer.save()
 
    return Response(serializer.data)

@api_view(['POST', "GET"])
def updateContract(request, pk):
    contract = Contract.objects.get(id=pk)
    Contract.objects.update()
    serializer = ContractSerializer(instance=contract, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteContract(request, pk):
    contract = Contract.objects.get(id=pk)
    contract.delete()

    return Response(f'{contract} deleted')