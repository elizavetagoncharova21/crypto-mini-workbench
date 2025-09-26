import json
from app.price import get_price

def calculate_portfolio(path: str):
    with open(path, "r") as f:
        data = json.load(f)
    total = 0
    for coin in data.get("holdings", []):
        symbol = coin["id"]
        amount = coin["amount"]
        price = get_price(symbol)
        value = amount * price
        total += value
        print(f"{symbol.upper():8} {amount:8} x ${price:10.2f} = ${value:10.2f}")
    print("-" * 40)
    print(f"Total: ${total:.2f}")
