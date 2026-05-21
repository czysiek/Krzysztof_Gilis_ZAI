from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import FinancialAsset
from .serializers import FinancialAssetSerializer
from .services import fetch_and_save_asset

class FinancialAssetViewSet(viewsets.ModelViewSet):
 #crud
    queryset = FinancialAsset.objects.all().order_by('-last_updated')
    serializer_class = FinancialAssetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # 1. Filtrowanie dokładne
    filterset_fields = ['asset_type', 'ticker']
    # 2. Wyszukiwanie "luzem"
    search_fields = ['name', 'ticker']
    # 3. Sortowanie
    ordering_fields = ['current_price_pln', 'last_updated', 'ticker']


    def perform_create(self, serializer):
        instance = serializer.save()
        fetch_and_save_asset(instance.ticker, instance.name, instance.asset_type)
