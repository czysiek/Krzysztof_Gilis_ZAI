#d7mejv9r01qngrvnu60gd7mejv9r01qngrvnu610

import requests


def get_stock_price(ticker):
    api_key = "d7mejv9r01qngrvnu60gd7mejv9r01qngrvnu610"
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data.get('c')
        if price == 0:
            print("Błąd: Nie znaleziono danych.")
            return None

        print(f"Aktualna cena {ticker} to: {price} USD")
        return price
    else:
        print(f"Błąd z Finnhub. Kod statusu: {response.status_code}")
        return None


if __name__ == "__main__":
    get_stock_price("AAPL")