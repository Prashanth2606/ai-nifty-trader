from broker.dhan_client import get_dhan_client
from datetime import datetime
import pandas as pd


class TrendAnalyzer:

    def __init__(self):
        self.dhan = get_dhan_client()

    def get_intraday_data(self):

        today = datetime.now().strftime("%Y-%m-%d")

        response = self.dhan.intraday_minute_data(
            security_id="13",
            exchange_segment="IDX_I",
            instrument_type="INDEX",
            from_date=today,
            to_date=today,
            interval=5
        )

        return response

    def get_trend(self):

        response = self.get_intraday_data()

        data = response["data"]

        df = pd.DataFrame({
            "close": data["close"]
        })

        df["ema20"] = (
            df["close"]
            .ewm(span=20, adjust=False)
            .mean()
        )

        df["ema50"] = (
            df["close"]
            .ewm(span=50, adjust=False)
            .mean()
        )

        price = float(df.iloc[-1]["close"])
        ema20 = float(df.iloc[-1]["ema20"])
        ema50 = float(df.iloc[-1]["ema50"])

        score = 0

        if price > ema20:
            score += 1

        if ema20 > ema50:
            score += 1

        if score == 2:
            trend = "STRONG UPTREND"

        elif score == 1:
            trend = "UPTREND"

        elif score == 0 and price < ema20 and ema20 < ema50:
            trend = "STRONG DOWNTREND"

        else:
            trend = "DOWNTREND"

        return {
            "price": round(price, 2),
            "ema20": round(ema20, 2),
            "ema50": round(ema50, 2),
            "trend": trend,
            "trend_score": score
        }