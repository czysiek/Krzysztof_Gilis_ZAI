# market_data/services.py
import requests
from .models import FinancialAsset
from decimal import Decimal


def get_usd_to_pln():
    url = "https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json"
    try:
        response = requests.get(url)
        data = response.json()
        return Decimal(str(data['rates'][0]['mid']))
    except:
        return Decimal('4.00')  # Kurs awaryjny


def fetch_and_save_asset(ticker, name, asset_type='STOCK'):
    # 1. API KEY
    FINNHUB_TOKEN = "d7mejv9r01qngrvnu60gd7mejv9r01qngrvnu610"
    # 2. Pobieranie ceny z Finnhub
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={FINNHUB_TOKEN}"

    try:
        response = requests.get(url)
        price_usd = Decimal(str(response.json().get('c', 0)))

        if price_usd == 0:
            print(f"Błąd: Nie znaleziono ceny dla {ticker}")
            return None

        # 3. Pobieranie kursu NBP
        rate = get_usd_to_pln()
        price_pln = price_usd * rate


        asset, created = FinancialAsset.objects.update_or_create(
            ticker=ticker,
            defaults={
                'name': name,
                'asset_type': asset_type,
                'price_usd': price_usd,
                'current_price_pln': price_pln,
            }
        )

        status = "Utworzono" if created else "Zaktualizowano"
        print(f"{status}: {ticker} ({price_usd} USD / {price_pln} PLN)")
        return asset

    except Exception as e:
        print(f"Wystąpił błąd dla {ticker}: {e}")
        return None