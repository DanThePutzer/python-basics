import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

HPI_Data = pd.read_pickle('8-Data/50statesPctRelative.pickle')

# Rolling Mean
# 12MA = 12 moving average -> Average between groups of 12
# Since data is monthly, that forms exactly the average of a year
# Up until number specified in rolling results will be NaN, since there are not enought datapoints yet to form an average
# (Need at least 12 datapoints to make an average between 12 datapoints lol)
HPI_Data['TX12MA'] = HPI_Data['TX'].rolling(12).mean()

# Rolling Standard Deviation
# High STD means things move around a lot more -> Volatility indicator
HPI_Data['TX12STD'] = HPI_Data['TX'].rolling(12).std()

# Rolling Correlation between two columns
TX_AK_CORR = HPI_Data['TX'].rolling(12).corr(HPI_Data['AK'])

print(HPI_Data['TX12MA'].head(20))

fig = plt.figure()
ax1 = plt.subplot2grid((4,4), (0,0), colspan=2, rowspan=2)
# sharex: will share axis with other selected subplot
ax2 = plt.subplot2grid((4,4), (0,2), colspan=2, rowspan=2)
ax3 = plt.subplot2grid((4,4), (2,0), colspan=4, rowspan=2)

HPI_Data[['TX', 'TX12MA']].plot(ax=ax1, lw=2.0)
HPI_Data['TX12STD'].plot(ax=ax2, lw=2.0, label='TX 12M STD')
TX_AK_CORR.plot(ax=ax3, lw=2.0, label='TX AK Correlation')

plt.legend(loc=4)
plt.show()