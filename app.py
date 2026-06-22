from market.quotes import MarketQuotes
from market.option_chain import OptionChain

print("=" * 50)
print("AI NIFTY OPTIONS TRADER")
print("=" * 50)

market = MarketQuotes()
oc = OptionChain()

spot = market.get_nifty()["last_price"]

# ONE API CALL ONLY
chain = oc.get_raw_chain()

atm = oc.get_atm_strike(chain, spot)

sr = oc.get_support_resistance(chain)

print()
print(f"NIFTY      : {spot}")
print(f"ATM        : {atm}")
print(f"SUPPORT    : {sr['support']}")
print(f"RESISTANCE : {sr['resistance']}")

print()
print(f"MAX PUT OI  : {sr['max_put_oi']}")
print(f"MAX CALL OI : {sr['max_call_oi']}")