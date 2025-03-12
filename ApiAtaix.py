import requests

def fetch_data(endpoint):
    """Получает данные с API ATAIX по указанному эндпоинту."""
    url = f"https://api.ataix.kz/api/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("result", [])  # Извлекаем только полезные данные
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе {endpoint}: {e}")
        return []

def display_currencies():
    """Выводит список валют и их количество."""
    currencies = fetch_data("currencies")
    if currencies:
        print("\nСписок валют:")
        for currency in currencies:
            print(currency)
        print(f"Всего валют: {len(currencies)}")

def display_symbols():
    """Выводит список торговых пар и их количество."""
    symbols = fetch_data("symbols")
    if symbols:
        print("\nСписок торговых пар:")
        for symbol in symbols:
            print(symbol)
        print(f"Всего торговых пар: {len(symbols)}")

def display_prices():
    """Выводит цены монет и токенов."""
    prices = fetch_data("prices")
    if prices:
        print("\nЦены монет и токенов:")
        for item in prices:
            if isinstance(item, dict) and "symbol" in item and "last" in item:
                print(f"{item['symbol']}: {item['last']}")
            else:
                print(f"Некорректная запись: {item}")

def main():
    display_currencies()
    display_symbols()
    display_prices()

if __name__ == "__main__":
    main()
