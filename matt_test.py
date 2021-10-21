import yfinance as yf
import pandas as pd

arr = [['AAV'], ['ABAC'], ['ABCW'], ['ABDC'], ['ABGB'], ['ABTL'], ['ABX'], ['ABY'], ['ACAS'], ['ACAT'], ['ACCU']]
df = pd.DataFrame(data=arr)

print(df)


# tickers = pd.read_csv('tickers/tickers.csv', sep=',', header=None, usecols=[1], skiprows=[0]) #reading the data by using Pandas library

# for ticker in tickers[1]:
#     ticker_string = str(ticker)
#     yf_ticker = yf.Ticker(ticker_string)
    
#     historical_data = msft.history(period="max",intervals="1d") 
#     # print(historical_data) 

#     #Lets get this to an excel file
#     #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html (Documentation on this)
#     ticker_name = "msft"
#     file_name = "historical_data/" + ticker_name + ".csv"
#     historical_data.to_csv(file_name)

# # print(type(df))
