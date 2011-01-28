import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table fieldingof (
                playerID text,
                yearID integer,
                stint integer,
                Glf integer,
                Gcf integer,
                Grf integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('FieldingOF.csv', 'rb'), delimiter=',')

to_db = [(i['playerID'], i['yearID'], i['stint'], i['Glf'], i['Gcf'], \
          i['Grf']) \
          for i in data]

c.executemany("""insert into fieldingof (playerID, yearID, stint, Glf,
                    Gcf, Grf) 
                    values (?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
