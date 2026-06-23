from market.trend_analyzer import TrendAnalyzer
from pprint import pprint

ta = TrendAnalyzer()

pprint(
    ta.get_trend()
)