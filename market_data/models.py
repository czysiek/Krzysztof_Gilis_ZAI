from django.db import models

# Create your models here.
from django.db import models


class FinancialAsset(models.Model):
    ASSET_TYPES = [
        ('STOCK', 'Akcja'),
        ('ETF', 'Fundusz ETF'),
        ('KRYPTO','Kryptowaluta')
    ]

    ticker = models.CharField(max_length=10, unique=True, help_text="Symbol giełdowy, np. AAPL")
    name = models.CharField(max_length=100, help_text="Pełna nazwa spółki lub funduszu")
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES, default='STOCK')

    price_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_price_pln = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if self.price_usd is not None:
            from market_data.services import get_usd_to_pln
            aktualny_kurs = get_usd_to_pln()
            self.current_price_pln = self.price_usd * aktualny_kurs

        super().save(*args, **kwargs)