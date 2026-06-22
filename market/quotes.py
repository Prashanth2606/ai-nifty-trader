from broker.dhan_client import get_dhan_client


class MarketQuotes:

    def __init__(self):
        self.dhan = get_dhan_client()

    def get_nifty(self):

        response = self.dhan.quote_data(
            securities={
                "IDX_I": [13]
            }
        )

        quote = response["data"]["data"]["IDX_I"]["13"]

        return {
            "last_price": quote["last_price"],
            "open": quote["ohlc"]["open"],
            "high": quote["ohlc"]["high"],
            "low": quote["ohlc"]["low"],
            "close": quote["ohlc"]["close"],
            "change": quote["net_change"],
            "time": quote["last_trade_time"]
        }