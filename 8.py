# 8. Access the nested key ‘salary’ from the following JSON

import json

sampleJson = '''{
    "company":{
        "employee01":{
            "name":"emma",
            "payable":{
                "salary":7000,
                 "bonus":800
            }
        },

         "employee02":{
            "name":"joey",
            "payable":{
                "salary":8000,
                 "bonus":900
            }
        },

         "employee03":{
            "name":"rach",
            "payable":{
                "salary":9000, 
                "bonus":1000
            }
        }
    }
}'''


def access_sal(data):
    for a,first in data.items():
        for b,second in first.items():
            print(second['payable']['salary'])


data = json.loads(sampleJson)
access_sal(data)
