import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# Not using Housing Market Dataset for this one
# Instead bridge distance to ground, trying to hanlde erroneous data

bridge_height = {'Meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

# Turn object into a dataframe
df = pd.DataFrame(bridge_height)
df['STD'] = df['Meters'].rolling(2).std()

# Getting mean standard deviation using describe 
df_std = df.describe()['Meters']['std']

# Comparison Operator: Dataframe gets populated only with rows where the standard deviaton 'STD' is smaller than the mean STD determined above -> Outliers will be cut
df = df[ (df['STD'] < df_std) ]

print(df)

# print(df.head())

df['Meters'].plot()
plt.show()