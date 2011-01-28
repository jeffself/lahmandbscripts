import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table fieldingpost (
                playerID text,
                yearID integer,
                teamID text,
                lgID text,
                round text,
                POS text,
                G integer,
                GS integer,
                InnOuts integer,
                PO integer,
                assists integer,
                errors integer,
                DP integer,
                TP integer,
                PB integer,
                SB integer,
                CS integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('FieldingPost.csv', 'rb'), delimiter=',')

to_db = [(i['playerID'], i['yearID'], i['teamID'], i['lgID'], i['round'], \
          i['POS'], i['G'], i['GS'], i['InnOuts'], i['PO'], i['A'], i['E'], \
          i['DP'], i['TP'], i['PB'], i['SB'], i['CS']) \
          for i in data]

c.executemany("""insert into fieldingpost (playerID, yearID, teamID, lgID,
                    round, POS, G, GS, InnOuts, PO, assists, errors, DP, TP, 
                    PB, SB, CS) 
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
