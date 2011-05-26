import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table salary (
                yearID integer,
                teamID text,
                lgID text,
                playerID text,
                salary integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('Salaries.csv', 'rb'), delimiter=',')

to_db = ((i['yearID'], i['teamID'], i['lgID'], i['playerID'], i['salary'])
          for i in data)

c.executemany("""insert into salary (yearID, teamID, lgID, playerID, salary)
                values (?, ?, ?, ?, ?);""", to_db)

con.commit()
