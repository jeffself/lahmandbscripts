import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table allstars (
                playerID text,
                yearID integer,
                lgID text)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('Allstar.csv', 'rb'), delimiter=',')

to_db = [(i['playerID'], i['yearID'], i['lgID']) for i in data]

c.executemany("""insert into allstars (playerID, yearID, lgID) values (?, ?, ?);""", to_db)

con.commit()
