import sqlite3
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# Connection Setup
con = sqlite3.connect('Database.db')
c = con.cursor()

def graphData():
  c.execute("SELECT datestamp, value FROM plotStuff WHERE value < 20")
  # Turn data from SQLite query into pandas dataframe
  data = pd.DataFrame(c.fetchall())
  data.columns = ['Date', 'Value']
  # Plot data according to data
  # ls: line style
  # marker: type of shape that marks a point
  plt.plot_date(data['Date'], data['Value'], ls='-', marker='o')
  plt.show()

graphData()