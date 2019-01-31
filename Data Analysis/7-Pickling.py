import pandas as pd
import quandl
import pickle

# - - Copied from 4-Building_Dataset.py - - 
# Quandl API Key
apiKey = 'yPnE7yZqyJzdxcz1pVeh'

# Fetching data from HTML table on Wikipedia
def stateList():
  statesData = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
  statesDf = statesData['Name &postal abbreviation[1]']['Name &postal abbreviation[1].1']
  return statesDf

# - - Beginning 7-Pickling - - 

# General Dataframe to load Quandl data into

def grabInitialData():
  mainDf = pd.DataFrame()
  states = stateList()

  for state in states:
    query = 'FMAC/HPI_' + state
    df = quandl.get(query, authtoken=apiKey)
    # Need to rename column to state name because otherwise columns for each state will have same name -> Error
    df.rename(columns={'NSA Value': str(state)}, inplace=True)
    # Drop SA column, not needed (Never forget inplace!!! otherwise changes will be made to new df instead of current)
    df.drop('SA Value', axis=1, inplace=True)

    if mainDf.empty:
      mainDf = df
    else:
      mainDf = mainDf.join(df)

    print(state + ' done')

  print(mainDf.head())

  # Exporting mainDf Dataframe with pickle
  # Create pickle file with intention to write (wb)
  # b: binary
  # w: write
  # w+: deletes file and then opens (overrides it)
  # r: read
  # r+: read & write without overriding
  pickle_out = open('7-Data/50states.pickle', 'wb')
  # Saves mainDf to file created with pickle_out from above
  pickle.dump(mainDf, pickle_out)
  # Closes pickle_out and 'disconnects' file
  pickle_out.close()

  print('Pickle done')

# Run function once to load data and save with pickle
# grabInitialData()

# Importing pickle file with mainDf data
pickle_in = open('7-Data/50states.pickle', 'rb')
# Loads data from file grabbed in pickle_in into dataframe HPI_data
HPI_data = pickle.load(pickle_in)

# - - Pickling with Pandas instead of native python - -
# Requires fewer lines of code
# Saving to pickle file
HPI_data.to_pickle('7-Data/50states_pandas.pickle')
# Loadinf from pickle file
HPI2_data = pd.read_pickle('7-Data/50states_pandas.pickle')