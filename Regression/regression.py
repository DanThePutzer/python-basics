import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

# Fetching Data for Google Stock
df = quandl.get('WIKI/GOOGL')

# Defining and filling dataframe with initial columns
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Defining new, more meaningful features
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100
df['PCT_CHG'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

# Updating dataframe with final columns
df = df[['Adj. Close', 'HL_PCT', 'PCT_CHG', 'Adj. Volume']]

# Defining column used to forecast and filling up NaNs
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# Round forecasts to up to next full number
forecast_out = int(math.ceil(0.01*len(df)))

# Label column is forecast column shifted upwards (Acting as the actual future value to which we compare our model's output)
df['Label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())