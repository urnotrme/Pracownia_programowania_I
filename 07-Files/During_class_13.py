import json
with open("example_1.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)