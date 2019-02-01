import pandas as pd
import numpy as np
from statistics import mean

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

HousingData = pd.read_pickle('HPIDataset.pickle')
HousingData = HousingData.pct_change()

# Defining label value for each column
# 1: HPI goes up
# 0: HPI goes down
def labeling(currentHPI, futureHPI):
  if (currentHPI < futureHPI):
    return 1
  else:
    return 0

def moving_average(values):
  return mean(values)

# Shifting HPI USA column down by 1 month -> is "future" data for each row
HousingData['Future HPI USA'] = HousingData['HPI USA'].shift(-1)

# Replacing finifinite values and dropping NaN
# .replace: NumPy function, can replace stuff with syntax seen below
HousingData.replace([np.inf, -np.inf], np.nan, inplace=True)
HousingData.dropna(inplace=True)

# Mapping function to every row of dataframe
# First parameter is the function
# Following parameters are the input parameters for the function
HousingData['Label'] = list(map(labeling, HousingData['HPI USA'], HousingData['Future HPI USA']))
HousingData.to_pickle('15-Data/LabeledDataset.pickle')

print(HousingData.head(20))


# Rolling Apply Example
# RollingApply = HousingData['M30'].rolling(10).apply(moving_average, raw=True)
# print(RollingApply.tail())