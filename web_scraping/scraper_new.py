import pytrends
from pytrends.request import TrendReq

def trends(keyword):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe="today 12-m", geo="CA", gprop="")
    trends_data = pytrends.interest_over_time()
    return trends_data

print(trends("suit jacket"))
print(trends("suit"))
print(trends("dress shirt"))
print(trends("dress pants"))
print(trends("slacks"))
print(trends("dress shirt"))