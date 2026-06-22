from market.quotes import MarketQuotes

print("=" * 50)
print("AI NIFTY OPTIONS TRADER")
print("=" * 50)

market = MarketQuotes()

nifty = market.get_nifty()

print(f"NIFTY      : {nifty['last_price']}")
print(f"OPEN       : {nifty['open']}")
print(f"HIGH       : {nifty['high']}")
print(f"LOW        : {nifty['low']}")
print(f"PREV CLOSE : {nifty['close']}")
print(f"CHANGE     : {nifty['change']}")
print(f"TIME       : {nifty['time']}")