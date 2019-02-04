import sqlite3

# Defining connection to db file
# If file doesn't exist at given place, new file will be created
con = sqlite3.connect('Database.db')
c = con.cursor()

def createTable():
  # c.execute: Executes SQL command at cursor c
  # Recommended: Although SQL is not case sensitive, writing actual SQL commands in alls caps and everything else, like file names etc in lower case is good practice
  # - - Creating Table:
  # Command: CREATE TABLE IF NOT EXISTS
  # TableName(... columns go here like this: keyword: DATATYPE ...)
  c.execute("CREATE TABLE IF NOT EXISTS plotStuff(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def insertEntry():
  # - - Adding Entry:
  # Command: INSERT INTO
  # TableName(... entries for each column in correct order ...)
  # String values have to be in ''
  c.execute("INSERT INTO plotStuff VALUES(145689566, '05-02-2019', 'Statistics Deadline', 16)")
  # Write changes to db
  con.commit()

  # Close cursor and connection to free up used RAM
  c.close()
  con.close()

# createTable()
# insertEntry()