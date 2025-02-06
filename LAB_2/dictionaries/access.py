thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x)
#Same as:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")

print(x)

#DOBAVIL
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change Чисто ключи

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values() #Чисто значения

print(x) #before the change

car["year"] = 2020
car["color"] = "red"

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items() #вернет как туплы в листе

print(x) #before the change

car["year"] = 2020
car["color"] = "red"

print(x) #after the change