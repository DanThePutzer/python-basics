import pandas as pd
import quandl

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# Quandl API Key
apiKey = 'yPnE7yZqyJzdxcz1pVeh'

# Fetching data from Quandl
# Mortgage Interest Rate
def mortgage_30y():
  MORTG = quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken=apiKey)
  MORTG.columns = ['M30']
  MORTG.to_pickle('13-Data/Mortgage30y.pickle')

  # Turning actual datapoints into percent change
  MORTG['M30'] = (MORTG['M30'] - MORTG['M30'][0])/MORTG['M30'][0] * 100
  MORTG.to_pickle('13-Data/Mortgage30yPctRelative.pickle')

  # print(MORTG.head())
  return MORTG

# mortgage_30y()


# Loading data from pickle so we dont have to connect to quandl every time
MORTG_Data = pd.read_pickle('13-Data/Mortgage30yPctRelative.pickle')
MORTG_Data = MORTG_Data.resample('D').mean()
MORTG_Data = MORTG_Data.resample('M').mean()

HPI_Data = pd.read_pickle('8-Data/50statesPctRelative.pickle')

HPI_Bench = pd.read_pickle('8-Data/EntireUSAPctRelative.pickle')
HPI_Bench.columns = ['HPI USA']

HPI_M30 = HPI_Data.join(MORTG_Data)
# print(HPI_M30.corr()['M30'].describe())

fig = plt.figure()
ax1 = plt.subplot2grid((3,1), (0,0))
ax2 = plt.subplot2grid((3,1), (1,0), rowspan=2)

print(HPI_M30.head())
# print(MORTG_Data.head())

HPI_Bench.plot(ax=ax1, sharex=ax2)
MORTG_Data.plot(ax=ax2, color='r')

plt.legend()
plt.show()