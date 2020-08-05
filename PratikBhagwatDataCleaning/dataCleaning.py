import pandas as pd

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



connection = connector.connect(user='root', password='root',
                              host="localhost",
                              database='BigDataAnalytics')

dataFrame = pd.read_sql("select * from finaldataset",con=connection)


companies = set(dataFrame["Company"])

for company in companies:
    companyDf = pd.read_sql("select * from finaldataset where company = " + "\""+str( company ) + "\"" ,con = connection)

    check = companyDf["Date"].duplicated()


    print(ch)