
from django.core.management.base import BaseCommand
from market_data.models import FinancialAsset
from market_data.services import fetch_and_save_asset


class Command(BaseCommand):
    help = 'Importuje słownik startowy i aktualizuje wszystkie aktywa w bazie'

    def handle(self, *args, **kwargs):
        starter_dictionary = {
            'AAPL': ('Apple Inc.', 'STOCK'),
            'MSFT': ('Microsoft Corp.', 'STOCK'),
            'NVDA': ('NVIDIA Corp.', 'STOCK'),
            'TSLA': ('Tesla Inc.', 'STOCK'),
            'SPY': ('SPDR S&P 500 ETF Trust', 'ETF'),
        }

        self.stdout.write(self.style.WARNING("Sprawdzam słownik startowy"))

        for ticker, (name, a_type) in starter_dictionary.items():
            fetch_and_save_asset(ticker, name, a_type)

        custom_assets = FinancialAsset.objects.exclude(ticker__in=starter_dictionary.keys())

        if custom_assets.exists():
            self.stdout.write(
                self.style.WARNING(f"\n Aktualizuję {custom_assets.count()} aktywów spoza słownika"))
            for asset in custom_assets:
                fetch_and_save_asset(asset.ticker, asset.name, asset.asset_type)
        else:
            self.stdout.write(self.style.SUCCESS("\n Brak dodatkowych aktywów do aktualizacji."))

        self.stdout.write(self.style.SUCCESS("\n Masowy import zakończony sukcesem"))