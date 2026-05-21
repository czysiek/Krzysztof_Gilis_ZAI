import requests


def get_usd_to_pln():
    url = "http://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json"
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][0]['mid']
        print(f"Aktualny kurs USD wg NBP to: {rate} PLN")
        return rate
    else:
        print(f"Błąd podczas pobierania danych. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    get_usd_to_pln()