#! /usr/bin/env python

import sys
import unittest
from unittest import TestSuite

from create_json_from_path import addPathToPopulatedDict
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

class TestDictionaryReconstruction(unittest.TestCase):

  def setUp(self):
    pass

  def test_emptyDict_addADict(self):
    expectedOutput = {
        "from": {
          "mars": {
            "plan": {
              "locality": "City"
              }
            }
          }
        }

    inputPath = "/from/mars/plan/locality"
    inputPathValue = "City"
    input=addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_emptyDict_addOverSizedList(self):
    expectedOutput = {
        "from": {
          "mars": {
            "colony": [
              None,
              None,
              {
                "my": "City"
                }
              ]
            }
          }
        }

    inputPath = "/from/mars/colony/2/my"
    inputPathValue = "City"
    input=addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_emptyDict_addNestedList(self):
    expectedOutput = {
        "from": {
          "mars": {
            "colony": [
              [
                {
                  "my": [
                    "City"
                    ]
                  }
                ]
              ]
            }
          }
        }

    inputPath = "/from/mars/colony/0/0/my/0"
    inputPathValue = "City"
    input=addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendElement_inList(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              "Travel"
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/2"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendElement_inList_inSpecificLoc(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              None,
              "Travel"
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/3"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendList_nestedDict(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              {
                "outdoor": "Travel"
                }
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/2/outdoor"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict, 
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendOverSizedList_nestedDict(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              None,
              None,
              {
                "outdoor": "Travel"
                }
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/4/outdoor"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendNestedList_nestedDict(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              [
                {
                  "outdoor": "Travel"
                  }
                ]
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/2/0/outdoor"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendNestedOverSizedList_nestedDict(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              [
                None,
                None,
                None,
                None,
                None,
                {
                  "outdoor": "Travel"
                  }
                ]
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/2/5/outdoor"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendMultiple_NestedLists(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              [
                [
                  "Travel"
                  ]
                ]
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/2/0/0"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendMultiple_Oversied_NestedLists(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play",
              [
                None,
                None,
                None,
                None,
                [
                  None,
                  None,
                  None,
                  None,
                  None,
                  None,
                  None,
                  "Travel"
                  ]
                ]
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          }
        }

    inputPath = "/from/person/hobbies/2/4/7"
    inputPathValue = "Travel" 
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendaDict_atSecondLevel(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play"
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status",
          "mars": "City"
          }
        }

    inputPath = "/from/mars"
    inputPathValue = "City"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendNestedDict_atSecondLevel(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play"
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status",
          "mars": {
            "plan": {
              "locality": "City"
              }
            }
          }
        }

    inputPath = "/from/mars/plan/locality"
    inputPathValue = "City"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_existingDict_appendNestedDict_atRootLevel(self):
    expectedOutput = {
        "id": "X999_Y999",
        "from": {
          "name": "Anonymous",
          "id": "X12",
          "person": {
            "home": "London",
            "work": {
              "company": "private",
              "business": "IT"
              },
            "hobbies": [
              "sleep",
              "play"
              ]
            },
          "message": "Looking forward to 2010!",
          "type": "status"
          },
        "mars": {
          "plan": {
            "locality": [
              {
                "London": "City"
                }
              ]
            }
          }
        }

    inputPath = "/mars/plan/locality/0/London"
    inputPathValue = "City"
    input = addPathToPopulatedDict(testDict,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

class TestListReconstruction(unittest.TestCase):

  def setUp(self):
    pass

  def test_emptyList_appendDict_at_firstLevel(self):
    expectedOutput = [
        {
          "mars": {
            "plan": {
              "locality": "City"
              }
            }
          }
        ]

    inputPath = "/0/mars/plan/locality"
    inputPathValue = "City"
    input = addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_emptyList_appendDict_at_nonExisting_index(self):
    expectedOutput = [
        None,
        None,
        {
          "mars": {
            "plan": {
              "locality": "City"
              }
            }
          }
        ]

    inputPath = "/2/mars/plan/locality"
    inputPathValue = "City"
    input = addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_emptyList_appendNestedList_andDict(self):
    expectedOutput = [
        [
          {
            "mars": {
              "plan": {
                "locality": "City"
                }
              }
            }
          ]
        ]

    inputPath = "/0/0/mars/plan/locality"
    inputPathValue = "City"
    input = addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_emptyList_appendNestedList_andDict_andList(self):
    expectedOutput = [
        [
          {
            "mars": {
              "plan": [
                {
                  "locality": "City"
                  }
                ]
              }
            }
          ]
        ]

    inputPath = "/0/0/mars/plan/0/locality"
    inputPathValue = "City"
    input = addPathToPopulatedDict({},
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendDict_atExistingIndex(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ]
            },
          "from": {
            "person": {
              "hobbies": "Travel"
              }
            }
          },
        [
          "microsoft",
          "amazon"
          ]
        ]

    inputPath = "/2/from/person/hobbies"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendDict_atRoot(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ]
            }
          },
        [
          "microsoft",
          "amazon"
          ],
        {
          "from": {
            "person": {
              "hobbies": "Travel"
              }
            }
          }
        ]

    inputPath = "/4/from/person/hobbies"
    inputPathValue = "Travel" 
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendDict_overSizing_root(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ]
            }
          },
        [
          "microsoft",
          "amazon"
          ],
        None,
        {
          "from": {
            "person": {
              "hobbies": "Travel"
              }
            }
          }
        ]

    inputPath = "/5/from/person/hobbies"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendDict_nestedList_atSpecific_level(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ]
            },
          "from": {
            "person": {
              "hobbies": [
                [
                  [
                    [
                      "Travel"
                      ]
                    ]
                  ]
                ]
              }
            }
          },
        [
          "microsoft",
          "amazon"
          ]
        ]

    inputPath = "/2/from/person/hobbies/0/0/0/0"
    inputPathValue = "Travel"
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendDict_atSpecific_level(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ],
            "car": {
              "BMW": "anotherTest"
              }
            }
          },
        [
          "microsoft",
          "amazon"
          ]
        ]

    inputPath = "/2/person/car/BMW"
    inputPathValue = "anotherTest" 
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendNestedDictList_specificLevel(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize",
              [
                {
                  "site": {
                    "yahoo": "anotherTest"
                    }
                  }
                ]
              ]
            }
          },
        [
          "microsoft",
          "amazon"
          ]
        ]

    inputPath = "/2/person/hobbies/2/0/site/yahoo"
    inputPathValue = "anotherTest"
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendNestedList_overSizing_root(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ]
            }
          },
        [
          "microsoft",
          "amazon"
          ],
        [
          None,
          None,
          {
            "google": [
              {
                "uff": "anotherTest"
                }
              ]
            }
          ]
        ]

    inputPath = "/4/2/google/0/uff"
    inputPathValue = "anotherTest"
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

  def test_ExistingList_appendNestedList_overSizing_root_and_nestedStructure(self):
    expectedOutput = [
        "yahoo",
        "hotmail",
        {
          "person": {
            "name": "rob",
            "job": "computer",
            "hobbies": [
              "cycle",
              "excersize"
              ]
            }
          },
        [
          "microsoft",
          "amazon"
          ],
        None,
        None,
        [
          None,
          None,
          None,
          None,
          None,
          {
            "google": [
              None,
              None,
              {
                "uff": "anotherTest"
                }
              ]
            }
          ]
        ]

    inputPath = "/6/5/google/2/uff"
    inputPathValue = "anotherTest"
    input = addPathToPopulatedDict(testDict2,
        inputPath.split("/")[1:], inputPathValue)
    self.assertEqual(True, input == expectedOutput)

if __name__ == '__main__':
  test_cases = [TestDictionaryReconstruction, TestListReconstruction]

  testSuite = TestSuite()
  testLoader = unittest.TestLoader()

  for test_class in test_cases:
    tests = testLoader.loadTestsFromTestCase(test_class)
    testSuite.addTests(tests)


  result = unittest.TextTestRunner(verbosity=2).run(testSuite)
  test_exit_code = 0 if result.wasSuccessful() else 1
  sys.exit(test_exit_code)




