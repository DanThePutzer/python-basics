import pandas as pd
import quandl

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# Quandl API Key
apiKey = 'yPnE7yZqyJzdxcz1pVeh'

def get_unemployment():
  UNEMPL_US = quandl.get('EIA/STEO_XRUNR_M', authtoken=apiKey)
  UNEMPL_US.columns = ['UMPT']
  UNEMPL_US.to_pickle('14-Data/Unemployment.pickle')

  UNEMPL_US['UMPT'] = (UNEMPL_US['UMPT'] - UNEMPL_US['UMPT'][0])/UNEMPL_US['UMPT'][0] * 100
  UNEMPL_US.to_pickle('14-Data/UnemploymentPctRelative.pickle')

def get_GDP():
  GDP = quandl.get('BCB/4385', authtoken=apiKey)
  GDP.columns = ['GDP']
  GDP.to_pickle('14-Data/GDP.pickle')

  GDP['GDP'] = (GDP['GDP'] - GDP['GDP'][0])/GDP['GDP'][0] * 100
  GDP.to_pickle('14-Data/GDPPctRelative.pickle')


get_unemployment()
get_GDP()