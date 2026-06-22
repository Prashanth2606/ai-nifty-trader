from market.quotes import MarketQuotes
from market.option_chain import OptionChain

print("=" * 50)
print("AI NIFTY OPTIONS TRADER")
print("=" * 50)

market = MarketQuotes()
oc = OptionChain()

spot = market.get_nifty()["last_price"]

chain = oc.get_raw_chain()

atm = oc.get_atm_strike(chain, spot)

sr = oc.get_support_resistance(chain)

pcr = oc.get_pcr(chain)

oi = oc.get_atm_oi_analysis(chain, atm)

if pcr > 1.1:
    bias = "BULLISH"

elif pcr < 0.9:
    bias = "BEARISH"

else:
    bias = "NEUTRAL"

print()

print(f"NIFTY       : {spot}")
print(f"ATM         : {atm}")

print()

print(f"SUPPORT     : {sr['support']}")
print(f"RESISTANCE  : {sr['resistance']}")

print()

print(f"PCR         : {pcr}")
print(f"BIAS        : {bias}")

print()

print(f"ATM CE OI       : {oi['ce_oi']}")
print(f"ATM CE CHANGE   : {oi['ce_change']}")

print()

print(f"ATM PE OI       : {oi['pe_oi']}")
print(f"ATM PE CHANGE   : {oi['pe_change']}")

print()

print(f"ATM SIGNAL      : {oi['signal']}")

print()
print("=" * 50)