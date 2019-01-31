import pandas as pd
import numpy as np
import quandl

import matplotlib

# Matplotlib fix again
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# Quandl API Key
apiKey = 'yPnE7yZqyJzdxcz1pVeh'

# Reading in data from pickle created in 7-Pickling
HPI_Data = pd.read_pickle('7-Data/50states.pickle')
# Standard percent change: computes percent change relative to previous element
# HPI_Data = HPI_Data.pct_change()

# Percent change relative to first element
states = np.array(pd.read_csv('4-Data/statesShort.csv'))

for state in states:
  # Getting first value in each column
  # For some reason needed to use .iloc to be able to search by index instead of key
  # [0][0] because need value [0] in row [0]
  firstEntry = HPI_Data[state].iloc[0][0]
  HPI_Data[state] = (HPI_Data[state] - firstEntry)/firstEntry * 100

# Exporting percent change to new pickle
HPI_Data.to_pickle('8-Data/50statesPctRelative.pickle')

# Get data for entire US as a whole as benchmark
def HPI_Benchmark():
  df = quandl.get('FMAC/HPI_USA', authkey=apiKey)
  df.drop('SA Value', axis=1, inplace=True)
  df.rename(columns={'NSA Value': 'USA'}, inplace=True)
  df.to_pickle('8-Data/EntireUSA.pickle')

  df['USA'] = (df['USA'] - df['USA'][0])/df['USA'][0] * 100

  df.to_pickle('8-Data/EntireUSAPctRelative.pickle')

  # df.plot(lw=1.5)
  # plt.legend().remove()
  # plt.show()
  return df


# Plotting everything together
def plotAllData():
  individual = pd.read_pickle('8-Data/50statesPctRelative.pickle')
  benchmark = HPI_Benchmark()

  # Create a new pyplot figure
  fig = plt.figure()
  # Create subplot to plot graphs in
  ax1 = plt.subplot2grid((1,1),(0,0))

  # Plotting both dataframes in the same subplot
  # 'lw' = line width
  HPI_Data.plot(ax=ax1, lw=1.5)
  benchmark.plot(ax=ax1, lw=6, color='k')

  # Hides legend in plots
  plt.legend().remove()
  plt.show()

# Create correlation Table
HPI_Correlation = HPI_Data.corr()
print(HPI_Correlation.describe())