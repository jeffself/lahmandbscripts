import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table fielding (
                playerID text,
                yearID integer,
                stint integer,
                teamID text,
                lgID text,
                POS text,
                G integer,
                GS integer,
                InnOuts integer,
                PO integer,
                assists integer,
                errors integer,
                DP integer,
                PB integer,
                WP integer,
                SB integer,
                CS integer,
                ZR integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('Fielding.csv', 'rb'), delimiter=',')

to_db = [(i['playerID'], i['yearID'], i['stint'], i['teamID'], i['lgID'], \
          i['POS'], i['G'], i['GS'], i['InnOuts'], i['PO'], i['A'], i['E'], \
          i['DP'], i['PB'], i['WP'], i['SB'], i['CS'], i['ZR']) \
          for i in data]

c.executemany("""insert into fielding (playerID, yearID, stint, teamID,
                    lgID, POS, G, GS, InnOuts, PO, assists, errors, DP, 
                    PB, WP, SB, CS, ZR) 
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
