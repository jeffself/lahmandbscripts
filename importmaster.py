import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')
con.text_factory = str
c = con.cursor()

# Create the Masters table
c.execute("""create table masters (lahmanID integer,
                                   playerID text,
                                   managerID text,
                                   hofID text,
                                   birthYear integer,
                                   birthMonth integer,
                                   birthDay integer,
                                   birthCountry text,
                                   birthState text,
                                   birthCity text,
                                   deathYear integer,
                                   deathMonth integer,
                                   deathDay integer,
                                   deathCountry text,
                                   deathState text,
                                   deathCity text,
                                   nameFirst text,
                                   nameLast text,
                                   nameNote text,
                                   nameGiven text,
                                   nameNick text,
                                   weight integer,
                                   height integer,
                                   bats text,
                                   throws text,
                                   debut date,
                                   finalGame date,
                                   college text,
                                   lahman40ID text,
                                   lahman45ID text,
                                   retroID text,
                                   holtzID text,
                                   bbrefID text)""")

# csv.DictReader uses the first line in the file as column headings by default
dr = csv.DictReader(open('Master.csv', 'rb'), delimiter=',')
to_db = [(i['lahmanID'], 
          i['playerID'], 
          i['managerID'], 
          i['hofID'], 
          i['birthYear'], 
          i['birthMonth'], 
          i['birthDay'],
          i['birthCountry'], 
          i['birthState'], 
          i['birthCity'], 
          i['deathYear'], 
          i['deathMonth'], 
          i['deathDay'],
          i['deathCountry'], 
          i['deathState'], 
          i['deathCity'], 
          i['nameFirst'], 
          i['nameLast'], 
          i['nameNote'], 
          i['nameGiven'], 
          i['nameNick'], 
          i['weight'],
          i['height'], 
          i['bats'], 
          i['throws'], 
          i['debut'], 
          i['finalGame'], 
          i['college'],
          i['lahman40ID'], 
          i['lahman45ID'], 
          i['retroID'], 
          i['holtzID'], 
          i['bbrefID'], 
          ) 
          for i in dr]
c.executemany("insert into masters (lahmanID, playerID, managerID, hofID, birthYear, birthMonth, birthDay, birthCountry, \
               birthState, birthCity, deathYear, deathMonth, deathDay, deathCountry, deathState, deathCity, nameFirst, \
               nameLast, nameNote, nameGiven, nameNick, weight, height, bats, throws, debut, finalGame, college, lahman40ID, \
               lahman45ID, retroID, holtzID, bbrefID) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

con.commit()
