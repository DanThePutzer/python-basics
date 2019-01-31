import pandas as pd
import numpy as np
import quandl

# Quandl API Key
apiKey = 'yPnE7yZqyJzdxcz1pVeh'

# Fetch data from Quandl
df = quandl.get("FMAC/HPI_CT", authtoken=apiKey)

# Fetching data from HTML table on Wikipedia
statesData = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
statesDf = statesData['Name &postal abbreviation[1]']['Name &postal abbreviation[1].1']

#Converting series to dataframe
statesDf = statesDf.to_frame()
# Renaming column
statesDf.rename(columns={'Name &postal abbreviation[1].1': 'Abbreviation'}, inplace=True)

# Write state abbreviations to CSV file
statesDf.to_csv('4-Data/statesShort.csv', index=False, header=True)

# random = pd.read_csv('4-Data/statesShort.csv', header=None)
# print(random[1])

# for state in statesDf:
#   print('FMAC/HPI_' + state)