import json
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
    }

with open("filename.json", "w") as f:
     json.dump(person, f, indent=2)
     
with open("filename.json", "r") as f:
    data=json.load(f)
    
print(data)