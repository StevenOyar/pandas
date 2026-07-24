import pandas as pd
import matplotlib.pyplot as plt


homeless_df = pd.read_csv('homeless.csv')

#  the first 5 rows of the dataset 
print(homeless_df.head())

# basic infomation 
print(homeless_df.info())

# name of the columns
print(homeless_df.columns
)
# description statistics of the dataset
print(homeless_df.describe())

