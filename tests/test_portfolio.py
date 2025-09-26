from app.portfolio import calculate_portfolio
import json, tempfile

def test_portfolio(tmp_path):
    data = {"holdings":[{"id":"bitcoin","amount":0.001}]}
    file = tmp_path / "p.json"
    file.write_text(json.dumps(data))
    calculate_portfolio(str(file))  # проверка, что функция не падает
