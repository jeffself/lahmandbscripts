import csv
import sqlite3

con = sqlite3.connect('baseballstats.db')

c = con.cursor()

# Create the table
c.execute("""create table appearances (yearID integer,
									   teamID text,
                                       lgID text,
                                       playerID text,
                                       G_all integer,
									   G_batting integer,
									   G_defense integer,
									   G_p integer,
									   G_c integer,
									   G_1b integer,
									   G_2b integer,
									   G_3b integer,
									   G_ss integer,
									   G_lf integer,
									   G_cf integer,
									   G_rf integer,
									   G_of integer,
									   G_dh integer,
									   G_ph integer,
									   G_pr integer)""")

# csv.DictReader uses the first line in the file as column headings by default
dr = csv.DictReader(open('Appearances.csv', 'rb'), delimiter=',')
to_db = [(i['yearID'], 
		  i['teamID'], 
		  i['lgID'], 
		  i['playerID'], 
		  i['G_all'], 
		  i['G_batting'], 
		  i['G_defense'], 
		  i['G_p'], 
		  i['G_c'], 
		  i['G_1b'], 
		  i['G_2b'], 
		  i['G_3b'], 
		  i['G_ss'], 
		  i['G_lf'],
		  i['G_cf'], 
		  i['G_rf'], 
		  i['G_of'], 
		  i['G_dh'], 
		  i['G_ph'], 
		  i['G_pr']) for i in dr]
c.executemany("insert into appearances (yearID, teamID, lgID, playerID, G_all, G_batting, G_defense, G_p, G_c, \
                                        G_1b, G_2b, G_3b, G_ss, G_lf, G_cf, G_rf, G_of, G_dh, G_ph, G_pr) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

con.commit()
