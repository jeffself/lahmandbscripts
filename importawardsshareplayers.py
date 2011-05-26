import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table awardsshareplayers (
                awardID text,
                yearID integer,
                lgID text,
                playerID text,
                pointsWon integer,
                pointsMax integer,
                votesFirst integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('AwardsSharePlayers.csv', 'rb'), delimiter=',')

to_db = ((i['awardID'], i['yearID'], i['lgID'], i['playerID'], \
          i['pointsWon'], i['pointsMax'], i['votesFirst']) for i in data)

c.executemany("""insert into awardsshareplayers (awardID, yearID, lgID, 
                    playerID, pointsWon, pointsMax, votesFirst) 
                    values (?, ?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
