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

    input=addPathToPopulatedDict({},
            ["from", "mars", "plan", "locality"], "City")
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

    input = addPathToPopulatedDict({},
              ["from", "mars", "colony", "2", "my"], "City")
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

    input = addPathToPopulatedDict({},
              ["from", "mars", "colony", "0", "0", "my", "0"], "City")
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
 
    input = addPathToPopulatedDict(testDict,
              ["from", "person", "hobbies", "2"], "Travel")
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

    input = addPathToPopulatedDict(testDict,
              ["from", "person", "hobbies", "3"], "Travel")
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

    input = addPathToPopulatedDict(testDict, ["from", "person", "hobbies", "2", "outdoor"], "Travel")
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

    input = addPathToPopulatedDict(testDict,
            ["from", "person", "hobbies", "4", "outdoor"], "Travel")
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

    input = addPathToPopulatedDict(testDict,
              ["from", "person", "hobbies", "2", "0", "outdoor"], "Travel")
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

    input = addPathToPopulatedDict(testDict,
              ["from", "person", "hobbies", "2", "5", "outdoor"], "Travel")
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

    input = addPathToPopulatedDict(testDict,
              ["from", "person", "hobbies", "2", "0", "0"], "Travel")
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

    input = addPathToPopulatedDict(testDict,
              ["from", "person", "hobbies", "2", "4", "7"], "Travel") 
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

    input = addPathToPopulatedDict(testDict,
              ["from", "mars"], "City")
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

    input = addPathToPopulatedDict(testDict,
              ["from", "mars", "plan", "locality"], "City")
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

    input = addPathToPopulatedDict(testDict,
              ["mars", "plan", "locality", "0", "London"], "City")
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

    input = addPathToPopulatedDict({},
              ["0", "mars", "plan", "locality"], "City")
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

    input = addPathToPopulatedDict({},
              ["2", "mars", "plan", "locality"], "City")
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

    input = addPathToPopulatedDict({},
              ["0", "0", "mars", "plan", "locality"], "City")
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

    input = addPathToPopulatedDict({},
              ["0", "0", "mars", "plan", "0", "locality"], "City")
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

    input = addPathToPopulatedDict(testDict2,
              ["2", "from", "person", "hobbies"], "Travel")
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

    input = addPathToPopulatedDict(testDict2,
             ["4", "from", "person", "hobbies"], "Travel") 
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

    input = addPathToPopulatedDict(testDict2,
              ["5", "from", "person", "hobbies"], "Travel")
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

    input = addPathToPopulatedDict(testDict2,
              ["2", "from", "person", "hobbies", "0", "0", "0", "0"], "Travel")
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

    input = addPathToPopulatedDict(testDict2,
              ["2", "person", "car", "BMW"], "anotherTest") 
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

    input = addPathToPopulatedDict(testDict2,
              ["2", "person", "hobbies", "2", "0", "site", "yahoo"], "anotherTest")
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

    input = addPathToPopulatedDict(testDict2,
              ["4", "2", "google", "0", "uff"], "anotherTest")
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

    input = addPathToPopulatedDict(testDict2,
              ["6", "5", "google", "2", "uff"], "anotherTest")
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




