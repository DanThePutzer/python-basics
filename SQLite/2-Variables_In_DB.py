import sqlite3
import time
import datetime
import random

# Connection Setup
con = sqlite3.connect('Database.db')
c = con.cursor()

# Function generates random entries using variables
def dynamicDataEntry():
  unix = time.time()
  date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
  keyword = 'Infinity Blade'
  value = random.randrange(0,100)

  # Insert variable values into new entry
  # Use syntax below:
  c.execute("INSERT INTO plotStuff (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
            (unix, date, keyword, value))
  con.commit()

# Run dynamicEntry 20 times
for i in range(20):
  dynamicDataEntry()
  time.sleep(0.2)

# Close connection to db
c.close()
con.close()