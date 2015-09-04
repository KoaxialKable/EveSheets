#! /usr/bin/env python
import sqlite3 as lite
import json
import constants

# Constants moved to separate file because they're big and unsightly.
DB_NAME            = constants.DB_NAME
SHUTTLE_NAMES      = constants.SHUTTLE_NAMES
DESIRED_PARTIALS   = constants.DESIRED_PARTIALS
DESIRED_ATTRIBUTES = constants.DESIRED_ATTRIBUTES
QUERY_STRING       = constants.QUERY_STRING


'''
  Get all one-word ship names
  Also get all two-word ship names that contain a word from DESIRED_PARTIALS
  ...and shuttles, because why not?
'''
def ship_is_desired(name):
  if ' ' in name:
    if (any(partial in name for partial in DESIRED_PARTIALS)) or (name in SHUTTLE_NAMES):
      return True
    return False
  return True


'''
  The records in the database have two columns for numeric values.
  Any time the valueFloat has a value, take that one over whatever might be in valueInt.
  Only take valueInt if valueFloat is empty.
'''
def extract_desired_information(record, ship_name):
  attribute_label = record[7]
  valueInt = record[9]
  valueFloat = record[10]

  for database_attribute_name, json_name in DESIRED_ATTRIBUTES.items():
    if attribute_label == database_attribute_name:
      outer_json[ship_name].update({json_name: int(valueInt) if valueFloat is None else int(valueFloat)})
      return



'''
  Go through every record returned by the query and
    format the entire JSON object in one pass
'''
def get_all_ships(dataset):
  current_ship_id = '0'
  for record in dataset:
    if (record[0] != current_ship_id) and ship_is_desired(record[1]):
      ship_name = record[1].title().replace(' ', '')
      outer_json[ship_name] = {"typeid": record[0], "faction": record[11], "class": record[2], "mass": int(record[3]), "volume": int(record[4]), "capacity": int(record[5])}
      current_ship_id = record[0]
    else:
      # Already have the base information, need to get desired attributes
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
formatted_json = json.dumps(outer_json, sort_keys=True, indent=2)

outfile = open('ships.json', 'w')
outfile.write(formatted_json)
print('Process completed successfully.')
