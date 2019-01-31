import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

HPI_Data = pd.read_pickle('8-Data/50statesPctRelative.pickle')

# Resampling Data from monthly to yearly
# A = Annualy
# .mean() = standard mean 
# .ohlc() = open high low close (gives 4 columns)
YearData = HPI_Data['TX'].resample('A').mean()

print(YearData.head())

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_Data['TX'].plot(ax=ax1, lw=1.0, label='Monthly TX HPI')
YearData.plot(ax=ax1, lw=1.0, label='Yearly TX HPI')
# 'loc' decides in which corner legend is shown
plt.legend(loc=2)
plt.show()