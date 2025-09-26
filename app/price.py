import requests

def get_price(coin_id: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    data = requests.get(url).json()
    return data.get(coin_id, {}).get("usd", 0.0)
