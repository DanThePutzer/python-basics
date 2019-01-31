# Using Dataframes and Numpy Arrays

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {
  'Day': [1,2,3,4,5,6],
  'Visitors': [43,53,34,45,64,34],
  'Bounce_Rate': [65,72,62,64,54,66]
}

# Create dataframe out of object(?)
df = pd.DataFrame(web_stats)

# Set selected column as index of dataframe
df.set_index('Visitors', inplace=True)

# Convert dataframe to list
test = df.Day.tolist()

# print(df)
# print(test)

# Create numoy array out of dataframe columns
np.array(df[['Day', 'Bounce_Rate']])

# Create dataframe out of numoy array (out of columns of another dataframe)
new_df = pd.DataFrame(np.array(df[['Day', 'Bounce_Rate']]))

print(new_df)

