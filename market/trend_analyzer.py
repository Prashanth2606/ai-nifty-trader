from broker.dhan_client import get_dhan_client


class TrendAnalyzer:

    def __init__(self):
        self.dhan = get_dhan_client()

    def get_raw_data(self):

        data = self.dhan.intraday_minute_data(
            security_id=13,
            exchange_segment="IDX_I",
            instrument_type="INDEX"
        )

        return data