import yfinance as yf
import pandas as pd

tickers = pd.read_csv('historical_data/A.csv', sep=',', header=None, skiprows=[0]) #reading the data by using Pandas library


print(tickers)

# BERT


# Ticker: A
# pass in the article to BERT for context analysis
    # gives some sort of numerical representation of connotation
        #Ex. "Company sold X amount of shares" --> 
            #Sell if you have the stock (sell connotation)
            #Buy if you do not have the stock (buy connotation)

# connotation/
    # A.csv
        # Date, Number (numerical representation of connotation)


# Merge historical_data and connotation
    # 8th column (all neutral value or empty)
        #Neutral values/Range:
        #Positive values/Range:
        #Negative values/Range:
        #No article (N/A): (maybe 2 or something)
    # go through connotation/A.csv
    # get date, edit the 8th column according to Number (numerical representation of connotation)

    # 9th column
        #publisher