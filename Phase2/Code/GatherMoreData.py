import pandas as pd
import numpy as np

data = pd.read_csv('Data/dataQuandlLarger.csv')

data1 = (data.loc[data['Date']>='2000-01-01'])

data = pd.read_csv('Data/dataYF1.csv')

data2 = (data.loc[data['Date']>='2000-01-01'])

data = pd.read_csv('Data/dataYF2.csv')

data3 = (data.loc[data['Date']>='2000-01-01'])

del data1['Adj. Open']
del data1['Adj. Low']
del data1['Adj. High']
del data1['Adj. Volume']

data2 = data2.rename(columns = {"Dividends" : "Ex-Dividend", "Splits" : "Split Ratio", "Adj Close" : "Adj. Close"})
data3 = data3.rename(columns = {"Dividends" : "Ex-Dividend", "Splits" : "Split Ratio", "Adj Close" : "Adj. Close"})
print(data2.head())
finalData = pd.DataFrame()
finalData = finalData.append(data1)
finalData = finalData.append(data2)
finalData = finalData.append(data3)

finalData.to_csv('MergedData.csv')