from rest_framework import serializers
from .models import FinancialAsset

class FinancialAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAsset
        fields = '__all__'