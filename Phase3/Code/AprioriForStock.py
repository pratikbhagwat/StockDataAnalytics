import pickle
from efficient_apriori import apriori

#Load the dump file containing the dataset
f = open('stockTransactions.dump','rb')

apriori_dataset = pickle.load(f)

print(apriori_dataset[0])

#Generate rules
itemsets, rules = apriori(apriori_dataset, min_support=0.3,  min_confidence=0.9)

print (rules)