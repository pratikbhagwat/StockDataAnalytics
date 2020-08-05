import pandas as pd
import pickle

data = pd.read_csv(r'C:\Users\nari9\OneDrive\Documents\PG\Assignments\Summer3\BDA\720-Project\720-Project\Data\MergedDataMoreSources.csv')


#Filter out data from year 2008 to 2009
data = (data[data['Date']>='2008'])

data = data[data['Date']<'2009']

data.to_csv('2008data.csv')
all_dates = data['Date'].unique()

adj_close_per_day = []
i = 0

#Get all Adj. Close prices into a list
for date in all_dates:
    #print (data[data['Date'] == date]['Adj. Close'])
    adj_close_per_day.append(data[data['Date'] == date]['Adj. Close'].tolist())
    #print (adj_close_per_day)

apriori_dataset = []
companies = data['Company'].unique()

#Check for each day and company if the current price is higher than the previous price
for i in range(1, len(adj_close_per_day)):
    l = []
    for j in range(0, 41):
        if (adj_close_per_day[i][j]>adj_close_per_day[i-1][j]):
            l.append(companies[j])
        
    apriori_dataset.append(tuple(l))

print (len(adj_close_per_day))

#Dump the dataset to a file
f = open('stockTransactions.dump', 'wb')
pickle.dump(apriori_dataset, f)

#apriori_dataframe = pd.DataFrame(apriori_dataset, columns=companies)

#apriori_dataframe.to_csv(r'C:\Users\nari9\OneDrive\Documents\PG\Assignments\Summer3\BDA\720-Project\720-Project\Data\Apriori2008Companies.csv')
