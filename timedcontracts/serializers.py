from rest_framework import serializers
from .models import Contract, Market

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'