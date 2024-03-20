#Transforms the Bank Data csv file into json format as a txt file and saves it in the same folder location

import numpy as np
from numpy import add
import pandas as pd

#Read the csv file to a data frame
df = pd.read_csv('Bank_Data.csv')

#Splitlines of the json into multiple rows
df['json'] = df.to_json(orient='records',lines=True).splitlines()

#Takes the json column and sets it as dfjson variable
dfjson = df['json']
print(dfjson)

#Saves the json output as a text file in the same file path
np.savetxt(r'./output.txt',dfjson.values,fmt='%s')

