import pandas as pd
import quandl

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# Quandl API Key
apiKey = 'yPnE7yZqyJzdxcz1pVeh'

def get_unemployment():
  UNEMP = quandl.get('EIA/STEO_XRUNR_M', authtoken=apiKey)
  UNEMP.columns = ['UNEMP']
  UNEMP.to_pickle('14-Data/Unemployment.pickle')

  UNEMP['UNEMP'] = (UNEMP['UNEMP'] - UNEMP['UNEMP'][0])/UNEMP['UNEMP'][0] * 100
  UNEMP.to_pickle('14-Data/UnemploymentPctRelative.pickle')

def get_GDP():
  GDP = quandl.get('BCB/4385', authtoken=apiKey)
  GDP.columns = ['GDP']
  GDP.to_pickle('14-Data/GDP.pickle')

  GDP['GDP'] = (GDP['GDP'] - GDP['GDP'][0])/GDP['GDP'][0] * 100
  GDP.to_pickle('14-Data/GDPPctRelative.pickle')

def get_SP500():
  SP500 = pd.read_csv('14-Data/SP500.csv')[['Date', 'Adj Close']]
  SP500.set_index('Date', inplace=True)
  SP500.columns = ['S&P 500']
  SP500['S&P 500'] = (SP500['S&P 500'] - SP500['S&P 500'][0])/SP500['S&P 500'][0] * 100
  SP500.to_pickle('14-Data/SP500PctRelative.pickle')

# get_unemployment()
# get_GDP()
# get_SP500()

# - - Loading data from pickles & CSV - -
UNEMP = pd.read_pickle('14-Data/UnemploymentPctRelative.pickle')
UNEMP = UNEMP.resample('D').mean()
UNEMP = UNEMP.resample('M').mean()

GDP = pd.read_pickle('14-Data/GDPPctRelative.pickle')
GDP = GDP.resample('D').mean()
GDP = GDP.resample('M').mean()

SP500 = pd.read_pickle('14-Data/SP500PctRelative.pickle')
# Need to convert Dates in index from string to an actual Date for resampling to work
# Can happen when Date from a standard column is made index of dataframe
SP500.index = pd.to_datetime(SP500.index)
SP500 = SP500.resample('M').mean()

HPI_Data = pd.read_pickle('8-Data/50statesPctRelative.pickle')
HPI_Bench = pd.read_pickle('8-Data/EntireUSAPctRelative.pickle')
HPI_Bench.columns = ['HPI USA']

# MORTG_Data = pd.read_pickle('13-Data/Mortgage30yPctRelative.pickle')
# MORTG_Data = MORTG_Data.resample('D').mean()
# MORTG_Data = MORTG_Data.resample('M').mean()

MORTG = pd.read_pickle('13-Data/Mortgage30yPctRelative.pickle')
# MORTG.columns = ['MORTG 30y']
MORTG = MORTG.resample('D').mean()
MORTG = MORTG.resample('M').mean()

# print(HPI_Data.head())
# print(HPI_Bench.head())
# print(MORTG.head())

FullDataset = HPI_Data.join([HPI_Bench, MORTG, UNEMP, GDP, SP500])
FullDataset.dropna(inplace=True)
FullDataset.to_pickle('HPIDataset.pickle')

BenchmarkDataset = HPI_Bench.join([MORTG, UNEMP, GDP, SP500])
BenchmarkDataset.dropna(inplace=True)


