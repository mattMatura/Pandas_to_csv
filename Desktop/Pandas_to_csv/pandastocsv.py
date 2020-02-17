import pandas as pd
#import numpy as np
from pandas import Series, DataFrame

excelfile = pd.ExcelFile('demo2.xlsx') #importing excel file using pandas
dd = excelfile.sheet_names #saving sheet names in excel file as a list
print(dd)

for i in dd: #iterating through sheets in excel file
    dframe2 = excelfile.parse(i) #parse sheet into a DataFrame
    print(dframe2) #print the dataframe
    dframe2.to_csv(i+'.csv', encoding='utf-8', index=False) #convert and save each sheet to different csv files
