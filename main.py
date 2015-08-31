#! /usr/bin/env python
import json
from pprint import pprint
import math

with open('ore_yields.json', encoding='utf-8') as ore_yields_file:
    ore_yields = json.loads(ore_yields_file.read())

with open('typeid_list.json', encoding='utf-8') as typeid_list_file:
    typeid_list = json.loads(typeid_list_file.read())


# pprint(ore_yields["Ochre"]["base_prefix"])

def getThoseMinerals(amount_of_ore_in_m3, ore_type):
  # print('With {vol} m3 of {ore}, you can reprocess {batches} batches.'.format(vol=amount_of_ore_in_m3, ore=ore_type, batches=ore_volume/100))
  ore_type = ore_type.loser()
  ore_volume = ore_yields[ore_type]["volume"]
  minerals = ore_yields[ore_type]["minerals"]
  batches = amount_of_ore_in_m3 / (ore_volume * 100)
  print('batches = {}'.format(batches))

  for name, amount in minerals.items():
    print('{name}: {amount:,.0f}'.format(name=name.title(), amount=(amount*0.724086*batches)))
    # print(name, amount*batches)

# getThoseMinerals(12000, 'ochre')

def find_ids_by_name(search_string):
  print("\nMatches for '{}':".format(search_string))
  for typeID, name in typeid_list.items():
    if search_string.lower() in name.lower():
      print('{:^12}{:<}'.format(typeID, name))

find_ids_by_name('cruc')

# print(ore_yields["veldspar"]["volume"])