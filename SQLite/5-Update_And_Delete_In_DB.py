import sqlite3

# Connection Setup
con = sqlite3.connect('Database.db')
c = con.cursor()

def update():
  c.execute("SELECT * FROM plotStuff")
  [print(row) for row in c.fetchall()]

  # Update all rows where value is lower than 50 and set value to 200
  c.execute("UPDATE plotStuff SET value = 200 WHERE value > 50")
  con.commit()

  c.execute("SELECT * FROM plotStuff")
  [print(row) for row in c.fetchall()]

def delete():
  # Delete all rows where value equals 200
  c.execute("DELETE FROM plotStuff WHERE value = 200")
  con.commit()

# update()
delete()