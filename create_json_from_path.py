#! /usr/bin/env python
import json, copy

def extendListSize(listToResize, desiredSize):
  currentSize = len(listToResize)
  increaseSize = desiredSize - currentSize
  if increaseSize > 0:
    listToResize.extend([None for _ in range(increaseSize)])
  return listToResize

def addPathToEmptyDict(elements, value, typeOfNextStep):

  try:
    firstElement = int(elements[0])
    newDict = []
    extendListSize(newDict, firstElement + 1)
  except ValueError:
    firstElement = elements[0]
    newDict = {}

  if len(typeOfNextStep) == 1:
    newDict[firstElement] = value
    return newDict

  newDictNext = {}
  for i, ele in enumerate(elements, start=1):
    try:
      ele = int(ele)
    except ValueError:
      ele = ele

    if i == 1:
      if typeOfNextStep[i] == "aList":
        if isinstance(newDict, list):
          newDict[ele] = []
        if isinstance(newDict, dict):
          newDict[ele] = []
      if typeOfNextStep[i] == "aDict":
        if isinstance(newDict, list):
          newDict[ele] = {}
        if isinstance(newDict, dict):
          newDict[ele] = {}
      newDictNext = newDict[ele]
    else:
      if i == len(elements):
        if isinstance(newDictNext, list):
          extendListSize(newDictNext, ele + 1)
          newDictNext[ele] =  value
        if isinstance(newDictNext, dict):
          newDictNext[ele] = value
      else:
        if isinstance(newDictNext, list):
          extendListSize(newDictNext, ele + 1)
          if typeOfNextStep[i] == "aList":
            if not newDictNext[ele]:
              newDictNext[ele] = []
          else:
            if not newDictNext[ele]:
              newDictNext[ele] = {}
          newDictNext = newDictNext[ele]
        else:
          if typeOfNextStep[i] == "aList":
            newDictNext[ele] = []
          else:
            newDictNext[ele] = {}
          newDictNext = newDictNext[ele]
  return newDict


def addPathToPopulatedDict(inputDict, elements, value):
  try:
    firstElement = int(elements[0])
    newDict = []
    extendListSize(newDict, firstElement + 1)
  except ValueError:
    firstElement = elements[0]
    newDict = {}

  typeOfNextStep = []
  for ele in elements:
    try:
      ele = int(ele)
      typeOfNextStep.append("aList")
    except ValueError:
      typeOfNextStep.append("aDict")

  # if inputDict = {}, that means we want to create new nested
  # dict
  if not inputDict:
    return addPathToEmptyDict(elements, value, typeOfNextStep)
  
  # if path to be added does not have origin in existing path
  if (not firstElement in inputDict) and isinstance(inputDict, dict):
    newNestedDict = addPathToEmptyDict(elements, value, typeOfNextStep)
    modifiedDict = copy.deepcopy(inputDict)
    modifiedDict[firstElement] = newNestedDict[firstElement]
    return modifiedDict

  # if path to be added have a origin in existing path
  newDictNext = copy.deepcopy(inputDict)
  modifiedDict = copy.deepcopy(inputDict)
  if (isinstance(modifiedDict, list)):
    extendListSize(modifiedDict, firstElement + 1)

  #newDict = {}
  for i, ele in enumerate(elements, start=1):
    try:
      ele = int(ele)
    except ValueError:
      ele = ele

    if i == 1:
      if isinstance(inputDict, list):
        try:
          firstElement = int(elements[0])
        except ValueError:
          pass
        if firstElement >= len(inputDict):
          changedElements = elements
          changedElements[0] = "0"
          newNestedDict = addPathToEmptyDict(changedElements, value, typeOfNextStep)
          modifiedDict = copy.deepcopy(inputDict)
          extendListSize(modifiedDict, firstElement + 1)
          modifiedDict[firstElement] = newNestedDict[0]
          return modifiedDict

        if firstElement < len(inputDict) and isinstance(inputDict[firstElement], dict):
          restElements = elements[1:]
          result = addPathToPopulatedDict(inputDict[firstElement], restElements, value)
          anotherTempDict = copy.deepcopy(inputDict)
          anotherTempDict[firstElement] = result
          return anotherTempDict

        if firstElement < len(inputDict) and isinstance(inputDict[firstElement], list):
          restElements = elements[1:]
          result = addPathToPopulatedDict(inputDict[firstElement], restElements, value)
          anotherTempDict = copy.deepcopy(inputDict)
          anotherTempDict[firstElement] = result
          return anotherTempDict

    if ele in newDictNext:
      if i == 1:
        newDict[ele] = newDictNext[ele]
        newDictNext = newDictNext[ele]
      else:
        newDictNext = newDictNext[ele]
    else:
      if i == len(elements):
        if isinstance(newDictNext, list):
          extendListSize(newDictNext, ele + 1)
          newDictNext[ele] =  value
        else:
          newDictNext[ele] = value
      else:
        if isinstance(newDictNext, list):
          extendListSize(newDictNext, ele + 1)

          if typeOfNextStep[i] == "aList":
            if not newDictNext[ele]:
              newDictNext[ele] = []
          else:
            if not newDictNext[ele]:
              newDictNext[ele] = {}
          newDictNext = newDictNext[ele]
        else:
          if typeOfNextStep[i] == "aList":
            newDictNext[ele] = []
          else:
            newDictNext[ele] = {}
          newDictNext = newDictNext[ele]
  modifiedDict[firstElement] = newDict[firstElement]
  return modifiedDict

if __name__ == '__main__':

  testDict = {
    "id": "X999_Y999",
    "from": {
      "name": "Tom Brady",
      "id": "X12",
      "person": {
        "home": "London",
        "work": {
          "company": "private",
          "business": "IT"
        },
        "hobbies": ["sleep", "play"],
    },
    "message": "Looking forward to 2010!",
    "type": "status",
    "name": "Anonymous"
    }
  }

  testDict2 = [
      "yahoo",
      "hotmail",
      {
        "person": {
        "name": "rob",
        "job": "computer",
        "hobbies": [ "cycle", "excersize" ]
        }
      },
      ["microsoft", "amazon"]
  ]
  testDict3 = {
  "infrastructure": {
    "availability_zones": [
      {
        "guid": "cb233561550d1f115251"
      },
    ]
  }
}


  def test1():
    print("========= Original Dict ========")
    print(json.dumps(testDict, indent=2))

    # create a brand new nested dict from scratch
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["from", "mars", "plan", "locality"], "City"), indent=2))

    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["from", "mars", "colony", "2", "my"], "City"), indent=2))

    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["from", "mars", "colony", "0", "0", "my", "0"], "City"), indent=2))
    # 
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({"from": {"person": {"home": "london"}}}, ["from", "person", "work", "business"], "IT"), indent=2))
    # 
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2"], "Travel"), indent=2))
    #
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "3"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2", "outdoor"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "4", "outdoor"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2", "0", "outdoor"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2", "5", "outdoor"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2", "0", "0"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2", "4", "7"], "Travel"), indent=2))

    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "mars"], "City"), indent=2))

    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["from", "mars", "plan", "locality"], "City"), indent=2))
    # 
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict, ["mars", "plan", "locality", "0", "London"], "City"), indent=2))


  def test2():
    print("========= Original Dict ========")
    print(json.dumps(testDict2, indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["0", "mars", "plan", "locality"], "City"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["2", "mars", "plan", "locality"], "City"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["0", "0", "mars", "plan", "locality"], "City"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict({}, ["0", "0", "mars", "plan", "0", "locality"], "City"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["2", "from", "person", "hobbies"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["4", "from", "person", "hobbies"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["5", "from", "person", "hobbies"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["2", "from", "person", "hobbies", "0", "0", "0", "0"], "Travel"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["2", "person", "car", "BMW"], "anotherTest"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["2", "person", "hobbies", "2", "0", "site", "yahoo"], "anotherTest"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["4", "2", "google", "0", "uff"], "anotherTest"), indent=2))
    #print("==================================================")
    #print(json.dumps(addPathToPopulatedDict(testDict2, ["6", "5", "google", "2", "uff"], "anotherTest"), indent=2))

  def test3():
    #print("==================================================")
    print(json.dumps(addPathToPopulatedDict(testDict3, ["infrastructure", "availability_zones", "0", "iaas_configuration_guid", "2"], "f06242d88fb38b8154b4"), indent=2))

  #test1()
  #test2()
  #test3()
