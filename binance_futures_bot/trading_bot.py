from binance import Client
from binance.enums import *
from logger import setup_logger

logger = setup_logger()

class TradingBot:
    def __init__(self, api_key, api_secret):
        self.live = bool(api_key and api_secret)

        if self.live:
            self.client = Client(api_key, api_secret)
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
            logger.info("Connected to Binance Futures Testnet (LIVE MODE)")
        else:
            self.client = None
            logger.info("Running in DRY-RUN MODE (No API keys)")

    def market_order(self, symbol, side, quantity):
        if not self.live:
            msg = f"[DRY RUN] MARKET {side} {quantity} {symbol}"
            logger.info(msg)
            return {"status": "DRY_RUN", "message": msg}

        order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        logger.info(order)
        return order

    def limit_order(self, symbol, side, quantity, price):
        if not self.live:
            msg = f"[DRY RUN] LIMIT {side} {quantity} {symbol} @ {price}"
            logger.info(msg)
            return {"status": "DRY_RUN", "message": msg}

        order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        logger.info(order)
        return order

    def stop_limit_order(self, symbol, side, quantity, price, stop_price):
        if not self.live:
            msg = f"[DRY RUN] STOP-LIMIT {side} {quantity} {symbol} @ {price} (stop {stop_price})"
            logger.info(msg)
            return {"status": "DRY_RUN", "message": msg}

        order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price,
            stopPrice=stop_price
        )
        logger.info(order)
        return order
