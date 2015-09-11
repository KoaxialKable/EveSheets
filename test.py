#! /usr/bin/env python
# print('Importing libraries...')
import requests
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import ElementTree
import sqlite3 as lite
import json
from pprint import pprint

# DB_NAME = 'salt.db'
# conn = lite.connect(DB_NAME)
# curs = conn.cursor()

# conn2 = lite.connect('salt.db')
# curs2 = conn2.cursor()

# r = curs.execute('select distinct p1 from match union select distinct p2 from match')
# r = curs.execute('select fighter, count(*) from bout group by fighter having count(fighter) > 2 order by count(fighter) desc')
# r = curs.execute('select t1.fighter, t2.outcome from bout as t1 join bout as t2 on t1.fighter = t2.fighter order by t1.fighter')
# r = curs.execute("select * from match where p1 = 'Black rugal' or p2 = 'Black rugal'")
# r = curs.execute("update match set duration = Null where matchID = 113")
# r = curs.execute("select winner, count(*) from match group by winner")
# r = curs.execute("select distinct fighter, outcome, duration from bout as b left join match as m on (b.fighter = m.p1 or b.fighter = m.p2) where b.fighter = 'Gaira'")
# r = curs.execute('select t1.p1, t1.p2, count(*) from match as t1 join match as t2 on (t1.p1 = t2.p1 and t1.p2 = t2.p2) group by t1.p1, t1.p2 having count(*) > 1')
# for row in r:
# 	print(row)
	# query = 'insert into bout (fighter, opponent, outcome) values (?, ?, ?)'
	# param = (row[0], row[1], row[2])
	# curs2.execute(query, param)
	# print('{:<24}{:<}'.format(row[0],row[1]))
# list_of_ships_to_scrape = ["Crucifier", "Raven"]

# DB_NAME = (r'..\myEVEdb.db')
# conn = lite.connect(DB_NAME)
# curs = conn.cursor()

# query = "select sum(skillpoints) from pilot_skill"
# curs.execute(query)
# for row in curs.fetchall():
#   print('{:,} total skillpoints'.format(int(row[0])))

json_data = open('ships.json')
Ships = json.load(json_data)
json_data.close()

classes = []

print("\nAll \"Amarr\" frigates with 3 or more med slots:")
for ship in Ships:
  if "med_slots" in Ships[ship]:
    # if Ships[ship]["med_slots"] >= 3 and ("Frigate" in Ships[ship]["class"] or Ships[ship]["class"] == "Interceptor" or Ships[ship]["class"] == "Covert Ops" or Ships[ship]["class"] == "Electronic Attack Ship") and Ships[ship]["faction"] == "Amarr":
    if ship == "Moros":
      print('{:<22} {}'.format(ship, Ships[ship]["class"]))

