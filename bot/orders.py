import logging

logger = logging.getLogger("trading_bot")

class OrderService:
    def __init__(self, client):
        self.client = client

    def create_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.place_order(**params)

            logger.info(f"Order response: {response}")

            return response

        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            raise
