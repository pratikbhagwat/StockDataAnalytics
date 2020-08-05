import yfinance as yf
import pandas as pd

#9 new companies
companies = {'AMD' : 'Advanced Micro Devices Inc', 
'MU' : 'Micron Technology Inc', 
'CSX' : 'CSX Corp', 
'AMAT' : 'Applied Materials Inc', 
'JD' : 'JD.com Inc ADR', 
'ATVI' : 'Activision Blizzard Inc', 
'ILMN' : 'Illumina Inc', 
'BIIB' : 'Biogen Inc', 
'ADSK' : 'Autodesk Inc'}

finalData = pd.DataFrame()
for key in companies.keys():
    #get Open, High, Low, Close, Adj Close, and Volume of each company
    data = yf.download(key,start='2000-01-01')
    #get Dividends and Splits of each company
    hist=yf.Ticker(key).history(start='2000-01-01')

    #add Dividends and Splits into the data
    data['Dividends']=hist['Dividends'].to_numpy()
    data['Splits']=hist['Stock Splits'].to_numpy()
    #add 'Company' attribute
    data['Company'] = companies[key]
    #add all the data of one company into the final dataframe
    finalData = finalData.append(data)
#export as csv
finalData.to_csv('dataYFmore1.csv')