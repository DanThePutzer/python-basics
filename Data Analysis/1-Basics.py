# Basic pandas setup and simple data reading from Yahoo
import pandas as pd
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()


df = web.DataReader("XOM", "yahoo", start, end)
df = df.drop("Adj Close", axis=1)

# Resetting and setting index
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

print(df.tail())

# Plotting data with matplotlib

# macOS matplotlib crash fix
import matplotlib
matplotlib.use("TkAgg") # Use TkAgg backend instead of macosx
from matplotlib import pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df["High"].plot()
plt.legend()
plt.show()