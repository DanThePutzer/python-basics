import pandas as pd

# Read in a CSV file and set Date column as index
df = pd.read_csv('3-Data/ZILLOW-Z77006_MLPAH.csv')
df.set_index('Date', inplace=True)

# print(df.head())

# Write first 10 rows into a new CSV file
df.head(10).to_csv('3-Data/shitboi.csv')

# Read file back in with Date set as index right away
# Index does not count as column anymore
df = pd.read_csv('3-Data/shitboi.csv', index_col=0)

# Rename Columns and save to new CSV
df.columns = ['Austin_HPI']
df.to_csv('3-Data/shitboi_chapter_2.csv')

# Save to CSV without header (= column names)
df.to_csv('3-Data/shitboi_chapter_3.csv', header=False)
# Read in CSV with no header
df = pd.read_csv('3-Data/shitboi_chapter_3.csv', names=['Date', 'Austin_HPI'], index_col=0)

# Write dataframe into HTML file
df.to_html('3-Data/example.html')

# Rename single column
df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)

print(df)