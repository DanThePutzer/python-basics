import sqlite3

# Connection Setup
con = sqlite3.connect('Database.db')
c = con.cursor()

def readDB():
  # SELECT command selects stuff in db (kinda like one selects text in an editor)
  # * means everything with no special filtering
  # Use WHERE to filter for certain criteria in columns
  # Could also just pull speciified columns by replacing * with for example unix, keywords
  c.execute("SELECT * FROM plotStuff WHERE value < 38 AND keyword = 'Infinity Blade'")
  # Assign the data selected by cursor to variable (Kinda like Strg + C)
  # fetchall() copies everything selected
  # fetchone() copies single row
  for row in c.fetchall():
    print(row)

readDB()