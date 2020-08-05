import quandl as quandl
import pandas as pd

#Api Key
quandl.ApiConfig.api_key = 'KiR8KAswuFtb_FFyj-mN'

#13 company Tickers
companies = {'AAPL': 'Apple Inc', 'MSFT': 'Microsoft Corp', 'AMZN': 'Amazon.com Inc', 'FB': 'Facebook Inc', 'GOOGL': 'Alphabet Inc', 'GOOG': 'Alphabet Inc', 'INTC': 'Intel Corp', 'NVDA': 'NVIDIA Corp', 'CSCO': 'Cisco Systems Inc', 'CMCSA': 'Comcast Corp', 'ADBE': 'Adobe Inc', 'NFLX': 'Netflix Inc', 'PEP': 'PepsiCo Inc', 'PYPL': 'PayPal Holdings Inc', 'TSLA': 'Tesla Inc', 'COST': 'Costco Wholesale Corp', 'AMGN': 'Amgen Inc', 'TMUS': 'T-Mobile US Inc', 'AVGO': 'Broadcom Inc', 'TXN': 'Texas Instruments Inc', 'CHTR': 'Charter Communications Inc', 'QCOM': 'QUALCOMM Inc', 'SBUX': 'Starbucks Corp', 'GILD': 'Gilead Sciences Inc', 'MDLZ': 'Mondelez International Inc', 'INTU': 'Intuit Inc', 'BKNG': 'Booking Holdings Inc', 'FISV': 'Fiserv Inc', 'ADP': 'Automatic Data Processing Inc', 'ISRG': 'Intuitive Surgical Inc', 'VRTX': 'Vertex Pharmaceuticals Inc', 'REGN': 'Regeneron Pharmaceuticals Inc'}
    
finalData = pd.DataFrame()

for key in companies.keys():

    data = quandl.get('WIKI/' + key, start_date = "2000-01-01")

    data['Company'] = companies[key]
    finalData = finalData.append(data)

#print (finalData)

finalData.to_csv('Data/dataQuandlLarger.csv')

