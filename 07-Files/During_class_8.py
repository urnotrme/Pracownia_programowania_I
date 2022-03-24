person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
    }

print(person)
print(person['name'])
print(person['hobby'])
print(person['surname']='Nowak')
print(person['married']=False)
print(person['married']= not person['married'])
print(person["gender"]= "male")
print(person['hobby'].append("bicycle"))
print(person["phone"]["work"]="313131444")