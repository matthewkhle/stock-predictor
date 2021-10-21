import yfinance as yf
import pandas as pd


tickers = pd.read_csv('tickers/tickers.csv', sep=',', header=None, usecols=[1], skiprows=[0]) #reading the data by using Pandas library

unfound_tickers = []

for ticker in tickers[1]:
    try:
        ticker_string = str(ticker)
        yf_ticker = yf.Ticker(ticker_string)
        
        historical_data = yf_ticker.history(period="max",intervals="1d") 
        if historical_data.empty:
            unfound_tickers.append([ticker_string])
        else:
            file_name = "historical_data/" + ticker_string + ".csv"
            historical_data.to_csv(file_name)
    except:
        print("ticker error")
        unfound_tickers.append([ticker_string])


unfound_tickers_df = pd.DataFrame(data=unfound_tickers)
unfound_tickers_df.to_csv("tickers/unfound_tickers.csv")
