#! /usr/bin/env python
import sqlite3 as lite
import json
import constants

DB_NAME            = constants.DB_NAME
SHUTTLE_NAMES      = constants.SHUTTLE_NAMES
DESIRED_PARTIALS   = constants.DESIRED_PARTIALS
DESIRED_ATTRIBUTES = constants.DESIRED_ATTRIBUTES
QUERY_STRING       = constants.QUERY_STRING

def ship_is_desired(name):
  if ' ' in name:
    if (any(partial in name for partial in DESIRED_PARTIALS)) or (name in SHUTTLE_NAMES):
      return True
    return False
  return True



def extract_desired_information(record, ship_name):
  # outer_json[ship_name].update({"capacitor_recharge_rate":record[9] if record[10] is None else int(record[10])})
  label = record[7]
  valueInt = record[9]
  valueFloat = record[10]

  for key, value in DESIRED_ATTRIBUTES.items():
    if label == key:
      outer_json[ship_name].update({value: int(valueInt) if valueFloat is None else int(valueFloat)})
      return



'''
Primary loop
Goes through every record returned by the query and formats the entire JSON object.
'''
def get_all_ships(dataset):
  current_ship_id = '0'
  for record in dataset:
    if (record[0] != current_ship_id) and ship_is_desired(record[1]):
      # print(record[0], record[1])
      ship_name = record[1].title().replace(' ', '')
      outer_json[ship_name] = {"typeid": record[0], "faction": record[11], "class": record[2], "mass": int(record[3]), "volume": int(record[4]), "capacity": int(record[5])}
      current_ship_id = record[0]
    else:
      # on to second record of the
      extract_desired_information(record, ship_name)
     




'''
*************

PROGRAM START

*************
'''
conn = lite.connect(DB_NAME)
curs = conn.cursor()
curs.execute(QUERY_STRING)
result_set = curs.fetchall()


outer_json = {}
get_all_ships(result_set)
j = json.dumps(outer_json, sort_keys=True, indent=2)
print(j)
