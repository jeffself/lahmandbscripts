import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table allstarsfull (playerID text,
                                       yearID integer,
									   gameNum integer,
									   teamID text,
                                       lgID text,
                                       GP integer,
                                       startingPos integer)""")

# csv.DictReader uses the first line in the file as column headings by default
dr = csv.DictReader(open('AllstarFull.csv', 'rb'), delimiter=',')
to_db = [(i['playerID'], i['yearID'], i['gameNum'], i['teamID'], i['lgID'], i['GP'], i['startingPos']) for i in dr]
c.executemany("insert into allstarsfull (playerID, yearID, gameNum, teamID, lgID, GP, startingPos) values (?, ?, ?, ?, ?, ?, ?);", to_db)

con.commit()
