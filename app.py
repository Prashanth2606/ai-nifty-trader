from market.option_chain import OptionChain

print("=" * 50)
print("AI NIFTY OPTIONS TRADER")
print("=" * 50)

# Initialize
oc = OptionChain()

# Fetch Option Chain Once
chain = oc.get_raw_chain()

# Live Spot Price
spot = chain["data"]["data"]["last_price"]

# Analytics
atm = oc.get_atm_strike(chain, spot)

# Near ATM Support / Resistance
sr = oc.get_near_atm_support_resistance(chain, atm)

# PCR
pcr = oc.get_pcr(chain)

# ATM OI Analysis
oi = oc.get_atm_oi_analysis(chain, atm)

# ----------------------------------
# MARKET SCORE ENGINE
# ----------------------------------

score = 0

# PCR
if pcr > 1:
    score += 1
else:
    score -= 1

# OI Signal
if oi["signal"] == "PUT WRITING":
    score += 1

elif oi["signal"] == "CALL WRITING":
    score -= 1

# Spot vs ATM
if spot > atm:
    score += 1

elif spot < atm:
    score -= 1

# Market View
if score >= 3:
    view = "STRONG BULLISH"

elif score == 2:
    view = "BULLISH"

elif score == 1:
    view = "SLIGHT BULLISH"

elif score == 0:
    view = "NEUTRAL"

elif score == -1:
    view = "SLIGHT BEARISH"

elif score == -2:
    view = "BEARISH"

else:
    view = "STRONG BEARISH"

# Recommendation
if score >= 2:
    recommendation = "BUY CALL"

elif score <= -2:
    recommendation = "BUY PUT"

else:
    recommendation = "NO TRADE"

# ----------------------------------
# OUTPUT
# ----------------------------------

print()

print(f"NIFTY          : {spot}")
print(f"ATM            : {atm}")

print()

print(f"SUPPORT        : {sr['support']}")
print(f"RESISTANCE     : {sr['resistance']}")

print()

print(f"PCR            : {pcr}")

print()

print(f"ATM CE OI      : {oi['ce_oi']}")
print(f"ATM CE CHANGE  : {oi['ce_change']}")

print()

print(f"ATM PE OI      : {oi['pe_oi']}")
print(f"ATM PE CHANGE  : {oi['pe_change']}")

print()

print(f"ATM SIGNAL     : {oi['signal']}")

print()

print(f"MARKET SCORE   : {score}")
print(f"MARKET VIEW    : {view}")

print()

print(f"RECOMMENDATION : {recommendation}")

print()
print("=" * 50)