import argparse
from app.price import get_price
from app.portfolio import calculate_portfolio

def main():
    parser = argparse.ArgumentParser(prog="crypto-mini-workbench")
    sub = parser.add_subparsers(dest="cmd")

    p = sub.add_parser("price")
    p.add_argument("--coin", type=str, default="bitcoin")

    pf = sub.add_parser("portfolio")
    pf.add_argument("file", type=str)

    args = parser.parse_args()

    if args.cmd == "price":
        price = get_price(args.coin)
        print(f"{args.coin.upper()} price: ${price:.2f}")
    elif args.cmd == "portfolio":
        calculate_portfolio(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
