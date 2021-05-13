#! /usr/bin/env python

import json, sys, yaml

def traverse(datadict):

  finalData = datadict

  def do_walk(datadict):
    if isinstance(datadict, dict):
      for key, value in datadict.items():
        if isinstance(value, dict):
          do_walk(value)
        if isinstance(value, list):
          do_walk(value)

    if isinstance(datadict, list):
      for i, key in enumerate(datadict, start=0):
        if key == None:
          del datadict[i]
      for i, key in enumerate(datadict, start=0):
        if isinstance(key, dict):
          do_walk(key)
        if isinstance(key, list):
          do_walk(key)

  do_walk(datadict)
  return finalData

if __name__ == '__main__':
  file = sys.argv[1]

  with open(file) as f:
    data = yaml.safe_load(f)
    if not data:
      data = json.load(f)

nullRemovedJson = traverse(data)

print(json.dumps(nullRemovedJson, indent=2, sort_keys=True))
