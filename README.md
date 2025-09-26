# Crypto Mini Workbench ⚙️

Мини-репозиторий с базовыми утилитами:
- Получение цен через CoinGecko
- Подсчёт портфеля из JSON
- CLI

## Быстрый старт
```bash
git clone https://github.com/YOUR_USERNAME/crypto-mini-workbench.git
cd crypto-mini-workbench
pip install -r requirements.txt
python -m app.cli price --coin bitcoin
python -m app.cli portfolio data/sample_portfolio.json
