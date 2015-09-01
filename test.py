#! /usr/bin/env python
# print('Importing libraries...')
import requests
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import ElementTree
import sqlite3 as lite
import json

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
list_of_ships_to_scrape = ["Condor", "Griffin", "Slasher", "Reaper", "Executioner", "Inquisitor", "Tormentor", "Oracle", "Crucifier", "Omen", "Maller", "Pilgrim", "Curse"]
outer_json = {}
for ship_name in list_of_ships_to_scrape:
	print('Working on {}'.format(ship_name))
	url_to_scrape = "http://wiki.eveuniversity.org/" + ship_name.replace(' ', '_')

	r = requests.get(url_to_scrape)
	root = ET.fromstring(r.text)

	current_ship = {}
	for row in root.findall('.//td[@class="att-line"]'):
		for cell in row.findall('.//div[@class="att-item"]'):
			for div in cell:
				if 'item att-label' in div.attrib.values():
					if div.text == "Low":
						name = "low_slots"
					elif div.text == "High":
						name = "high_slots"
					elif div.text == "Medium":
						name = "mid_slots"
					elif div.text == "Turrets":
						name = "turret_hardpoints"
					elif div.text == "Launchers":
						name = "launcher_hardpoints"
					elif div.text == "Sig. Radius":
						name = "signature_radius"
					elif div.text == "Scan Res.":
						name = "scan_resolution"
					elif div.text == "Shield Resistances":
						name = "shield_hitpoints"
					elif div.text == "Armor Resistances":
						name = "armor_hitpoints"
					elif div.text == "Max Tgt. Range":
						name = "max_targeting_range"
					else:
						name = div.text.replace(' ', '_').lower()
				if 'item att-value' in div.attrib.values():
					value = div.text.split()[0].replace(',', '')
			current_ship[name] = value
			# print(name, value)
		for cell in row.findall('.//div[@class="att-item highlight"]'):
			for div in cell:
				if 'item att-label' in div.attrib.values():
					if div.text == "Low":
						name = "low_slots"
					elif div.text == "High":
						name = "high_slots"
					elif div.text == "Medium":
						name = "mid_slots"
					elif div.text == "Turrets":
						name = "turret_hardpoints"
					elif div.text == "Launchers":
						name = "launcher_hardpoints"
					elif div.text == "Sig. Radius":
						name = "signature_radius"
					elif div.text == "Scan Res.":
						name = "scan_resolution"
					elif div.text == "Shield Resistances":
						name = "shield_hitpoints"
					elif div.text == "Armor Resistances":
						name = "armor_hitpoints"
					elif div.text == "Max Tgt. Range":
						name = "max_targeting_range"
					else:
						name = div.text.replace(' ', '_').lower()
				if 'item att-value' in div.attrib.values():
					value = div.text.split()[0]
			current_ship[name] = value
			# print(name, value)

	outer_json[ship_name] = current_ship
j = json.dumps(outer_json, sort_keys=True, indent=4)

print()
print(j)
