

import yfinance as yf
import pandas as pd
from yfinance import ticker

msft = yf.Ticker("MSFT")

#History
#Prints the data for opening, closing, low, close, volume, dividend, stock splits
historical_data = msft.history(period="max",intervals="1d") #returns <class 'pandas.core.frame.DataFrame'>
# print(historical_data) 

#Lets get this to an excel file
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html (Documentation on this)
ticker_name = "msft"
file_name = "historical_data/" + ticker_name + ".csv"
historical_data.to_csv(file_name)



# df = pd.read_csv('historical_data.csv', sep=',', header=None) #reading the data by using Pandas library
# print(type(df[0]))  #Collection of objects (if you call one subscript)

# download the csv from kaggle article dataset, get a list of unique tickers from the right column, for each ticker, generate csv of historical data




