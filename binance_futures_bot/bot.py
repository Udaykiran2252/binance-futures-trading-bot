from trading_bot import TradingBot
from config import API_KEY, API_SECRET

def main():
    print("\n=== Binance Futures Trading Bot ===\n")

    symbol = input("Symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY / SELL): ").upper()
    order_type = input("Order Type (MARKET / LIMIT / STOP): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = float(input("Limit Price: "))

    if order_type == "STOP":
        price = float(input("Limit Price: "))
        stop_price = float(input("Stop Price: "))

    bot = TradingBot(API_KEY, API_SECRET)

    if order_type == "MARKET":
        result = bot.market_order(symbol, side, quantity)
    elif order_type == "LIMIT":
        result = bot.limit_order(symbol, side, quantity, price)
    elif order_type == "STOP":
        result = bot.stop_limit_order(symbol, side, quantity, price, stop_price)
    else:
        print("Invalid order type")
        return

    print("\nRESULT:")
    print(result)

if __name__ == "__main__":
    main()
