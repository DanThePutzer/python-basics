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
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# Merging Dataframes
# Merges columns with same name, can merge on multiple columns to get best merged Dataframe
# Merging drops index, sometimes not ideal
merge = pd.merge(df1, df2, on=['HPI', 'Int_rate', 'US_GDP_Thousands'])
# print(merge)

# Joining Dataframes
# If index is important -> Use Join (Concatenate, Append & Merge ignore index)
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

join = df1.join(df3)
# print(join)



# Some more Messarounds
# Dataframes copied from Tutorial
df4 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})

df5 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})

# 'How' determines how DFs are merged:
# left: Indexes from first DF are used (in this case df4)
# right: Indexes from second DF are used (in this case df5)
# inner: All rows which would include some NaN after merging are dropped (default)
# outer: All rows are used regardless if NaN
merged = pd.merge(df4, df5, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print(merged)