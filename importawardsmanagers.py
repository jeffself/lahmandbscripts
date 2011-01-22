import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table awardsmanagers (
                managerID text,
                awardID text,
                yearID integer,
                lgID text,
                tie text,
                notes text)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('AwardsManagers.csv', 'rb'), delimiter=',')

to_db = [(i['managerID'], i['awardID'], i['yearID'], \
          i['lgID'], i['tie'], i['notes']) for i in data]

c.executemany("""insert into awardsmanagers (managerID, awardID, yearID, lgID,
                tie, notes)
                values (?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
