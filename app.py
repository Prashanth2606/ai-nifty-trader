from market.quotes import MarketQuotes
from market.option_chain import OptionChain

print("=" * 50)
print("AI NIFTY OPTIONS TRADER")
print("=" * 50)

# Initialize objects
market = MarketQuotes()
oc = OptionChain()

# Get spot price
spot = market.get_nifty()["last_price"]

# Get option chain once
chain = oc.get_raw_chain()

# Analytics
atm = oc.get_atm_strike(chain, spot)

sr = oc.get_support_resistance(chain)

pcr = oc.get_pcr(chain)

# Market Bias
if pcr > 1.1:
    bias = "BULLISH"

elif pcr < 0.9:
    bias = "BEARISH"

else:
    bias = "NEUTRAL"

# Output
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

print(f"MAX PUT OI  : {sr['max_put_oi']}")
print(f"MAX CALL OI : {sr['max_call_oi']}")

print()
print("=" * 50)