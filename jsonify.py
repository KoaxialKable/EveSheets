import sqlite3 as lite
import json

DB_NAME = './sqlite-latest.sqlite'
conn = lite.connect(DB_NAME)
curs = conn.cursor()

racial_shuttle_names = ['Amarr Shuttle', 'Caldari Shuttle', 'Gallente Shuttle', 'Minmatar Shuttle']
desired_partial_names = ['Navy', 'Fleet']
desired_attributes = {"armorHP": "armor_hitpoints", "capacitorCapacity": "capacitor_capacity", "rechargeRate": "capacitor_recharge_rate", "droneBandwidth": "drone_bandwidth", "droneCapacity": "drone_capacity", "cpuOutput": "cpu", "hiSlots": "high_slots", "lowSlots": "low_slots", "medSlots": "med_slots", "launcherSlotsLeft": "launcher_hardpoints", "powerOutput": "powergrid", "rigSlots": "rig_slots", "turretSlotsLeft": "turret_hardpoints", "techLevel": "tech_level", "requiredSkill1": "required_skill", "requiredSkill1Level": "required_skill_level", "shieldCapacity": "shield_hitpoints", "agility": "inertia_modifier", "maxVelocity": "max_velocity", "hp": "structure_hitpoints", "maxLockedTargets": "max_targets", "maxTargetRange": "max_targeting_range", "scanGravimetricStrength": "gravimetric_sensor_strength", "scanLadarStrength": "ladar_sensor_strength", "scanMagnetometricStrength": "magnetometric_sensor_strength", "scanRadarStrength": "radar_sensor_strength", "scanResolution": "scan_resolution", "signatureRadius": "signature_radius", "requiredSkill2": "required_advanced_skill", "requiredSkill2Level": "required_advanced_skill_level"}

query_string = (r"SELECT a.typeID AS 'invTypes.typeID', a.typeName AS 'invTypes.typeName', e.groupName, a.mass, a.volume, a.capacity, d.categoryName AS 'dgmAttributeCategories.categoryName', c.attributeName AS 'dgmAttributeTypes.attributeName', c.displayName, b.valueInt, b.valueFloat, f.raceName FROM invTypes AS a INNER JOIN dgmTypeAttributes AS b ON (a.typeID = b.typeID) INNER JOIN dgmAttributeTypes AS c ON (b.attributeID = c.attributeID) INNER JOIN dgmAttributeCategories as d ON (c.categoryID = d.categoryID) INNER JOIN invGroups as e ON (a.groupID = e.groupID) INNER JOIN chrRaces as f ON (a.raceID = f.raceID) WHERE e.categoryID = 6 AND c.attributeName NOT IN ('warpFactor', 'powerLoad', 'cpuLoad', 'powerToSpeed', 'mainColor', 'maxPassenger', 'propulsionGraphicID', 'gfxBoosterID') AND a.typeID NOT IN (34457, 34459, 34467, 34471) AND a.typeName NOT LIKE ('?%') ORDER BY a.TypeName, d.CategoryName, c.AttributeName")

curs.execute(query_string)
result_set = curs.fetchall()

outer_json = {}

def ship_is_desired(name):
  if ' ' in name:
    if (any(partial in name for partial in desired_partial_names)) or (name in racial_shuttle_names):
      return True
    return False
  return True

def extract_desired_information(record, ship_name):
  # outer_json[ship_name].update({"capacitor_recharge_rate":record[9] if record[10] is None else int(record[10])})
  label = record[7]
  valueInt = record[9]
  valueFloat = record[10]

  for key, value in desired_attributes.items():
    if label == key:
      outer_json[ship_name].update({value: int(valueInt) if valueFloat is None else int(valueFloat)})
      return

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
        


get_all_ships(result_set)
j = json.dumps(outer_json, sort_keys=True, indent=2)
print(j)
