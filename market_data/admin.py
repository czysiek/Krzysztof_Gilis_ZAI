from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FinancialAsset

@admin.register(FinancialAsset)
class FinancialAssetAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'name', 'asset_type', 'current_price_pln', 'last_updated')
    search_fields = ('ticker', 'name')
    list_filter = ('asset_type',)