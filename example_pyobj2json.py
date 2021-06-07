import json


data = [
    {
        "name": "alpha",
        "username": "alpha1",
        "id": 123,
        "location": {
            "district": "AAA",
            "subdistrict": "aaa"
        }
    },
    {
        "name": "beta",
        "username": "beta2",
        "id": 456,
        "location": {
            "district": "BBB",
            "subdistrict": "bbb"
        }
    },
    {
        "name": "gamma",
        "username": "gamma3",
        "id": 789,
        "location": {
            "district": "CCC",
            "subdistrict": "ccc"
        }
    }
]

dser = json.dumps(data)
print(dser, type(dser))

# serialize Python object to JSON object (no indentation; data is as a single line)
with open('pyobj2json.json', 'w') as example_json:
    json.dump(data, example_json)

# serialize Python object to JSON object with indentation
with open('pyobj2jsonindent.json', 'w') as example_json:
    json.dump(data, example_json, indent=2)
