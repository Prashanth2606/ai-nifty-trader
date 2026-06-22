from market.quotes import MarketQuotes
from market.option_chain import OptionChain

print("=" * 50)
print("AI NIFTY OPTIONS TRADER")
print("=" * 50)

# Initialize
market = MarketQuotes()
oc = OptionChain()

# Live Nifty Spot
spot = market.get_nifty()["last_price"]

# Fetch Option Chain Once
chain = oc.get_raw_chain()

# Analytics
atm = oc.get_atm_strike(chain, spot)

# Near ATM Support / Resistance
sr = oc.get_near_atm_support_resistance(chain, atm)

# PCR
pcr = oc.get_pcr(chain)

# ATM OI Analysis
oi = oc.get_atm_oi_analysis(chain, atm)

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

print(f"ATM CE OI       : {oi['ce_oi']}")
print(f"ATM CE CHANGE   : {oi['ce_change']}")

print()

print(f"ATM PE OI       : {oi['pe_oi']}")
print(f"ATM PE CHANGE   : {oi['pe_change']}")

print()

print(f"ATM SIGNAL      : {oi['signal']}")

print()
print("=" * 50)