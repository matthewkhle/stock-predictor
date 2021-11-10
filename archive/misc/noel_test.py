import yfinance as yf

data = yf.download("MSFT", start = "2017-01-01", end = "2017-01-04")
print(data)

msft = yf.Ticker("MSFT")


# Prints analyst recommandations for a given ticker.
# Overweight/Outperform = Stock will outperform other stocks in the relevant market sector/index. Good price/performance for 6-12 months. Given very carefully.
# Maybe ignore last column? Can't find out what main/up means though a majority of them do use main.
print(msft.recommendations)