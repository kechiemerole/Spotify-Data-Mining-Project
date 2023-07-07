# importing packages 
import json
import csv
import os
import pandas as pd


data = pd.read_csv("myDataCombined.csv")
print(data)
# Check for null values
null_values = data.isnull().sum()

# Print the number of null values for each column
print(null_values)