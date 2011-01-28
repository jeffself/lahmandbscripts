import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table halloffame (
                hofID text,
                yearid integer,
                votedBy text,
                ballots integer,
                needed integer,
                votes integer,
                inducted text,
                category text)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('HallOfFame.csv', 'rb'), delimiter=',')

to_db = [(i['hofID'], i['yearid'], i['votedBy'], i['ballots'], i['needed'], \
          i['votes'], i['inducted'], i['category']) \
          for i in data]

c.executemany("""insert into halloffame (hofID, yearid, votedBy, ballots,
                    needed, votes, inducted, category) 
                    values (?, ?, ?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
