import json
lijst = []
lijst.append({"name": "William", "lastName": "Jones"})
lijst.append({"name": "Anna", "lastName": "Ford"})

with open('result.json', 'w') as json_file:
    json.dump(lijst, json_file)

json_string = '[{"name": "William", "lastName": "Jones"}, {"name": "Anna", "lastName": "Ford"}]'