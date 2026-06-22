from broker.dhan_client import get_dhan_client


class OptionChain:

    def __init__(self):
        self.dhan = get_dhan_client()

    def get_raw_chain(self):

        return self.dhan.option_chain(
            under_security_id=13,
            under_exchange_segment="IDX_I",
            expiry="2026-06-23"
        )

    def get_atm_strike(self, chain, spot_price):

        option_data = chain["data"]["data"]["oc"]

        strikes = [float(strike) for strike in option_data.keys()]

        atm = min(
            strikes,
            key=lambda x: abs(x - spot_price)
        )

        return atm

    def get_support_resistance(self, chain):

        option_data = chain["data"]["data"]["oc"]

        max_call_oi = -1
        max_put_oi = -1

        resistance = None
        support = None

        for strike, values in option_data.items():

            strike_price = float(strike)

            ce_oi = values["ce"]["oi"]
            pe_oi = values["pe"]["oi"]

            if ce_oi > max_call_oi:
                max_call_oi = ce_oi
                resistance = strike_price

            if pe_oi > max_put_oi:
                max_put_oi = pe_oi
                support = strike_price

        return {
            "support": support,
            "resistance": resistance,
            "max_put_oi": max_put_oi,
            "max_call_oi": max_call_oi
        }