# json_manipulation

### Python version used
```bash
$ python --version
Python 3.9.0
```

## How to Run:
### `input_data_1.json` contents
```json
{
   "data": [
      {
         "id": "X999_Y999",
         "from": {
            "name": "Tom Brady", "id": "X12"
         },
         "message": "Looking forward to 2010!",
         "actions": [
            {
               "name": "Comment",
               "link": "http://www.facebook.com/X999/posts/Y999"
            },
            {
               "name": "Like",
               "link": "http://www.facebook.com/X999/posts/Y999"
            }
         ],
         "type": "status",
         "created_time": "2010-08-02T21:27:44+0000",
         "updated_time": "2010-08-02T21:27:44+0000"
      },
      {
         "id": "X998_Y998",
         "from": {
            "name": "Peyton Manning", "id": "X18"
         },
         "message": "Where's my contract?",
         "actions": [
            {
               "name": "Comment",
               "link": "http://www.facebook.com/X998/posts/Y998"
            },
            {
               "name": "Like",
               "link": "http://www.facebook.com/X998/posts/Y998"
            }
         ],
         "type": "status",
         "created_time": "2010-08-02T21:27:44+0000",
         "updated_time": "2010-08-02T21:27:44+0000"
      }
   ],
  "name": "Anonymous",
  "job": { "hobbyjob": [ "Gardening", "InteriorDesign"], "Fulltimejob": "Lawyer" }
}
```

### Generate Flat JSON structure
```bash
./generate_flat_json.py input_data_1.json > input_data_1_flat.json
```

#### `input_data_1_flat.json` file contents

```json
{
  "data/0/actions/0/link": "http://www.facebook.com/X999/posts/Y999",
  "data/0/actions/0/name": "Comment",
  "data/0/actions/1/link": "http://www.facebook.com/X999/posts/Y999",
  "data/0/actions/1/name": "Like",
  "data/0/created_time": "2010-08-02T21:27:44+0000",
  "data/0/from/id": "X12",
  "data/0/from/name": "Tom Brady",
  "data/0/id": "X999_Y999",
  "data/0/message": "Looking forward to 2010!",
  "data/0/type": "status",
  "data/0/updated_time": "2010-08-02T21:27:44+0000",
  "data/1/actions/0/link": "http://www.facebook.com/X998/posts/Y998",
  "data/1/actions/0/name": "Comment",
  "data/1/actions/1/link": "http://www.facebook.com/X998/posts/Y998",
  "data/1/actions/1/name": "Like",
  "data/1/created_time": "2010-08-02T21:27:44+0000",
  "data/1/from/id": "X18",
  "data/1/from/name": "Peyton Manning",
  "data/1/id": "X998_Y998",
  "data/1/message": "Where's my contract?",
  "data/1/type": "status",
  "data/1/updated_time": "2010-08-02T21:27:44+0000",
  "job/Fulltimejob": "Lawyer",
  "job/hobbyjob/0": "Gardening",
  "job/hobbyjob/1": "InteriorDesign",
  "name": "Anonymous"
}
```

### Re-generate JSON from flat JSON
```bash
./recreate_json_from_flat.py input_data_1_flat.json > recreated_data_1.json
```
#### `recreated_data_1.json` file contents
```json
{
  "data": [
    {
      "actions": [
        {
          "link": "http://www.facebook.com/X999/posts/Y999",
          "name": "Comment"
        },
        {
          "link": "http://www.facebook.com/X999/posts/Y999",
          "name": "Like"
        }
      ],
      "created_time": "2010-08-02T21:27:44+0000",
      "from": {
        "id": "X12",
        "name": "Tom Brady"
      },
      "id": "X999_Y999",
      "message": "Looking forward to 2010!",
      "type": "status",
      "updated_time": "2010-08-02T21:27:44+0000"
    },
    {
      "actions": [
        {
          "link": "http://www.facebook.com/X998/posts/Y998",
          "name": "Comment"
        },
        {
          "link": "http://www.facebook.com/X998/posts/Y998",
          "name": "Like"
        }
      ],
      "created_time": "2010-08-02T21:27:44+0000",
      "from": {
        "id": "X18",
        "name": "Peyton Manning"
      },
      "id": "X998_Y998",
      "message": "Where's my contract?",
      "type": "status",
      "updated_time": "2010-08-02T21:27:44+0000"
    }
  ],
  "job": {
    "Fulltimejob": "Lawyer",
    "hobbyjob": [
      "Gardening",
      "InteriorDesign"
    ]
  },
  "name": "Anonymous"
}
```
