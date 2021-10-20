import pandas as pd


# Only took tickers from one csv

# reading the data by using Pandas library
    # skip first row of column titles
    # only read column 3, where the tickers are
tickers = pd.read_csv('article_data/analyst_ratings_processed.csv', sep=',', header=None, usecols=[3], skiprows=[0]) 
tickers = tickers.drop_duplicates()

print(tickers)

tickers.to_csv("tickers/tickers.csv")