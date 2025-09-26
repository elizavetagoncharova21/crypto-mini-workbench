from app.price import get_price

def test_price_type():
    price = get_price("bitcoin")
    assert isinstance(price, float)
