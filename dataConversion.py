# importing packages 
import json
import csv
import os
import pandas as pd

# load first json file using pandas
df0 = pd.read_json('MyData/StreamingHistory0.json')

# view data
print(df0)

# load second json file using pandas
df1 = pd.read_json('MyData/StreamingHistory1.json')

# view data
print(df1)

# load third json file using pandas
df2 = pd.read_json('MyData/StreamingHistory2.json')

# view data
print(df2)

# use pandas.concat method
df = pd.concat([df0, df1,df2])

# view the concatenated dataframe
print(df)
 
# convert dataframe to csv file
df.to_csv("myDataCombined.csv",index=False)

# load the resultant csv file
result = pd.read_csv("myDataCombined.csv")

 
# and view the data
print(result)



