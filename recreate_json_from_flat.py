#! /usr/bin/env python

import json, sys, yaml, re
from collections import OrderedDict
from pprint import pprint
from create_json_from_path import addPathToPopulatedDict

file = sys.argv[1]

with open(file) as f:
  data = yaml.safe_load(f)
  if not data:
    data = json.load(f)

def do_walk():
  finalDict = {}

  for key, value in data.items():
    elements = key.split("/")
    finalDict = addPathToPopulatedDict(finalDict, elements, value)
  return finalDict


finalDict = do_walk()
print(json.dumps(finalDict, indent=2))

