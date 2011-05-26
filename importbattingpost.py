import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table battingpost (
                yearID integer,
                round text,
                playerID text,
                teamID text,
                lgID text,
                G integer,
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
                GIDP integer)""")

# csv.DictReader uses the first line in the file as column headings by default
data = csv.DictReader(open('BattingPost.csv', 'rb'), delimiter=',')

to_db = ((i['yearID'], i['round'], i['playerID'], i['teamID'], i['lgID'], \
          i['G'], i['AB'], i['R'], i['H'], i['2B'], i['3B'], i['HR'], \
          i['RBI'], i['SB'], i['CS'], i['BB'], i['SO'], i['IBB'], \
          i['HBP'], i['SH'], i['SF'], i['GIDP']) for i in data)

c.executemany("""insert into battingpost (yearID, round, playerID, teamID,
                    lgID, G, AB, R, H, Doubles, Triples, HR, RBI, 
                    SB, CS, BB, SO, IBB, HBP, SH, SF, GIDP) 
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)

con.commit()
