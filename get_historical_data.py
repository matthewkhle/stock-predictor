import yfinance as yf
import pandas as pd


tickers = pd.read_csv('tickers/tickers.csv', sep=',', header=None, usecols=[1], skiprows=[0]) #reading the data by using Pandas library

deprecated_tickers = []

for ticker in tickers[1]:
    ticker_string = str(ticker)
    yf_ticker = yf.Ticker(ticker_string)
    
    historical_data = yf_ticker.history(period="max",intervals="1d") 
    if historical_data.empty:
        deprecated_tickers.append([ticker_string])
    else:
        file_name = "historical_data/" + ticker_string + ".csv"
        historical_data.to_csv(file_name)


deprecated_tickers_df = pd.DataFrame(data=deprecated_tickers)


# ticker_string = str("BORN")
# yf_ticker = yf.Ticker(ticker_string)
# historical_data = yf_ticker.history(period="max",intervals="1d")
# # print(historical_data)
# if historical_data.empty:
#     print("its empty bro")
# else:
#     print("that's weird")
