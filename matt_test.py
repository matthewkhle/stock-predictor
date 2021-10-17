import pandas as pd

df = pd.read_csv('historical_data.csv', sep=',', header=None) #reading the data by using Pandas library

print(df[1])

# print(type(df))
