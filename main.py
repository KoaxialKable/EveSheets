#! /usr/bin/env python
import json
from pprint import pprint
import math

with open('ore_yields.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


# pprint(data["Ochre"]["base_prefix"])

def getThoseMinerals(amount_of_ore_in_m3, ore_type):
  # print('With {vol} m3 of {ore}, you can reprocess {batches} batches.'.format(vol=amount_of_ore_in_m3, ore=ore_type, batches=ore_volume/100))
  ore_volume = data[ore_type]["volume"]
  minerals = data[ore_type]["minerals"]
  batches = amount_of_ore_in_m3 / (ore_volume * 100)
  print('batches = {}'.format(batches))

  for name, amount in minerals.items():
    print('{name}: {amount:,.0f}'.format(name=name.title(), amount=(amount*0.724086*batches)))
    # print(name, amount*batches)

getThoseMinerals(12000, 'ochre')


# print(data["veldspar"]["volume"])