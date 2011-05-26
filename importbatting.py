import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table batting (
                playerID text,
                yearID integer,
                stint integer,
                teamID text,
                lgID text,
                G integer,
                G_batting integer,
                AB integer,
                R integer,
                H integer,
                Doubles integer,
                Triples integer,
                HR integer,
                RBI integer,
                SB integer,
                CS integer,
                BB integer,
                SO integer,
                IBB integer,
                HBP integer,
                SH integer,
                SF integer,
                GIDP integer,
                G_old integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('Batting.csv', 'rb'), delimiter=',')

to_db = ((i['playerID'], i['yearID'], i['stint'], i['teamID'], i['lgID'], \
          i['G'], i['G_batting'], i['AB'], i['R'], i['H'], i['2B'], \
          i['3B'], i['HR'], i['RBI'], i['SB'], i['CS'], i['BB'], \
          i['SO'], i['IBB'], i['HBP'], i['SH'], i['SF'], i['GIDP'], \
          i['G_old']) for i in data)

c.executemany("""insert into batting (playerID, yearID, stint, teamID,
                    lgID, G, G_batting, AB, R, H, Doubles, Triples, HR, RBI, 
                    SB, CS, BB, SO, IBB, HBP, SH, SF, GIDP, G_old) 
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
