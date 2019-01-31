import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


HPI_Data = pd.read_pickle('8-Data/50statesPctRelative.pickle')

HPI_Data['TX_Year'] = HPI_Data['TX'].resample('A').mean()

# Draw more graphs in one figure
fig = plt.figure()
# Create subplot2grid with size for all graphs in first brackets (Exp: (2,2) for 4 graphs)
# In second brackets specify position of subplot
# rowspan/colspan: specify how many rows/columns the subplot should occupy
ax1 = plt.subplot2grid((4,4), (0,0), rowspan=2, colspan=4)
ax2 = plt.subplot2grid((4,4), (2,0), rowspan=2, colspan=2)
ax3 = plt.subplot2grid((4,4), (2,2), rowspan=2, colspan=2)

# - - - - Handling Missing Data - - - -

# - - Method 1: Delete rows with NaN - -
# - Drop rows that include any amount NaN:
# df.dropna(inplace=True)
# - Only drop rows that have ALL NaNs:
# df.dropna(how='all', inplace=True)
# - Drop rows that have up to a certain amount (threshold) of NaNs:
# df.dropna(thresh=3, inplace=True)

# - - Method 2: Fill up NaN - -
# - Fill NaN using a method:
# df.fillna(method='ffill', inplace=True)
# ffill = forward fill -> takes data from previous column (past) and pushes it forward to fill NaN with it
# bfill = backward fill -> takes data from following column (future) and pulls it back to fill NaN with it
# -> bfill is more biased since it takes future data to fill NaN
# - Fill NaN with a value:
# df.fillna(value=-99999, limit=10, inplace=True)
# -> Used in machine learning so NaN will be treaded as an outlier
# -> limit: fills NaNs only up to this limit, all others stay NaNs


# Assign graphs to different subplots
HPI_Data_b = HPI_Data.fillna(method='bfill')
HPI_Data_b[['TX', 'TX_Year']].plot(ax=ax2, lw=1.0)
HPI_Data_f = HPI_Data.fillna(method='ffill')
HPI_Data_f[['TX', 'TX_Year']].plot(ax=ax1, lw=1.0)
HPI_Data_v = HPI_Data.fillna(value=-99999)
HPI_Data_v[['TX', 'TX_Year']].plot(ax=ax3, lw=1.0)
plt.legend()
plt.show()