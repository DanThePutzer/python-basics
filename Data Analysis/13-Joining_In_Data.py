import pandas
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
  # Turning actual datapoints into percent change
  MORTG['Value'] = (MORTG['Value'] - MORTG['Value'][0])/MORTG['Value'][0] * 100
  MORTG.to_pickle('13-Data/Mortgage30y.pickle')

  # print(MORTG.head())

mortgage_30y()