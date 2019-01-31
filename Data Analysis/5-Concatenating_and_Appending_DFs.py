import pandas as pd

# Dataframes copied from Tutorial
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# Concatenate Dataframes
# DF1 and DF2 have same columns, but different indices, so they can be concatenated
concat = pd.concat([df1, df2])
# print(concat)

# Appending Dataframes
# Basically same as Concatenate, but adds directly to dataframe instead of creating a new one
append = df1.append(df2)
# print(append)

# Adding series to dataframe
series = pd.Series([80, 2, 50], index=['HPI', 'Int_rate', 'US_GDP_Thousands']) # If index property missing will create new rows & columns with series data
df4 = df1.append(series, ignore_index=True)

print(df4)