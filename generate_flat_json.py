#! /usr/bin/env python

import json, sys, yaml, re
from collections import OrderedDict

file = sys.argv[1]

with open(file) as f:
  data = yaml.safe_load(f)
  if not data:
    data = json.load(f)

def createFlattenedJson(datadict):
  stack = []
  final_dict = OrderedDict()

  def do_walk(datadict):
    if isinstance(datadict, dict):
      sortedDict = OrderedDict(sorted(datadict.items()))
      datadict = sortedDict
      for key, value in datadict.items():
        stack.append(key)
        #print("/".join(stack))
        if isinstance(value, dict) and len(value.keys()) == 0:
          final_dict["/".join(stack)] = "EMPTY_DICT"
        if isinstance(value, list) and len(value) == 0:
          final_dict["/".join(stack)] = 'EMPTY_LIST'
        if isinstance(value, dict):
          do_walk(value)
        if isinstance(value, list):
          do_walk(value)
        if (not isinstance(value, dict)) and (not isinstance(value, list)):
          final_dict["/".join(stack)] = value
        stack.pop()

    if isinstance(datadict, list):
      n = 0
      for key in datadict:
        stack.append(str(n))
        n = n + 1
        if isinstance(key, dict):
          do_walk(key)
        if isinstance(key, list):
          do_walk(key)
        if (not isinstance(key, dict)) and (not isinstance(key, list)):
          final_dict["/".join(stack)] = key
        stack.pop()

  do_walk(datadict)
  return final_dict

def printKeys(dataDict):
  for key, value in dataDict.items():
    print(key)

def removeValueAndPrintUniqueKeys(dataDict):
  uniqueKeys = set()
  regex = re.compile('(.+)/value.*')
  for key, value in dataDict.items():
    result = regex.match(key)
    if result:
      uniqueKeys.add(result.group(1))
    else:
      uniqueKeys.add(key)
  for e in sorted(uniqueKeys):
    print(e)

flattenedJson = createFlattenedJson(data)

# prints original data in json format.
#print(json.dumps(data, indent=2, sort_keys=True))

# prints all data along with values in json flat structure.
print(json.dumps(flattenedJson, indent=2, sort_keys=True))

# prints all keys only
#printKeys(flattenedJson)

# prints keys after removing /value/ from path and remove duplicate as well
# removeValueAndPrintUniqueKeys(flattenedJson)
