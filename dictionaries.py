# CREATING DICT:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998
# }
# print(car)

# #or: by using dict() method:
# man=dict(name="John",age=22,country="Norway")
# print(man)

# #PRINTING AN ITEM:
# print(car["brand"])

# #or:
# x=car.get("model")
# print(x)

# #Duplicate values will overwrite existing values:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "year":1979,
#     "electric": False
# }
# print(car)

# #To determine how many items a dictionary has, use the len() function:
# print(len(car))
# print(type(car))


#Get Keys: The keys() method will return a list of all the keys in the dictionary.
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "year":1979,
#     "electric": False
# }
# x=car.keys()
# print(x)

# #Get Values: The values() method will return a list of all the values in the dictionary.
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "year":1979,
#     "electric": False
# }
# x=car.values()
# print(x)

#Get Items: The items() method will return each item in a dictionary, as tuples in a list.
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "year":1979,
#     "electric": False
# }
# x=car.items()
# print(x)

#Check if Key Exists:To determine if a specified key is present in a dictionary use the in keyword:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "year":1979,
#     "electric": False
# }
# if "model" in car:
#     print("Yes model is one of the keys in this dictionary")

    #Python - Change Dictionary Items"
    #Change Values: You can change the value of a specific item by referring to its key name:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# car["year"]=1979
# print(car)

#or by:Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# car.update({"year":1979})
# print(car)

#Remove Dictionary Items:
#1. The pop() method removes the item with the specified key name:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# car.pop("electric")
# print(car)

#2. The popitem() method removes the last inserted item:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# car.popitem()
# print(car)

#3. The del keyword removes the item with the specified key name:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# del car["electric"]
# print(car)

#The del keyword can also delete the dictionary completely:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# del car
# print(car)

#4. The clear() method empties the dictionary:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# car.clear()
# print(car)

# 5. Loop Through a Dictionary: You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary.
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }

# for x in car:
#     print(x)

# or:
# for x in car.keys():
#   print(x)

# #Print all values in the dictionary, one by one:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# # for x in car:
# #   print(car[x])

# # OR:
# # for x in car.values():
# #  print(x)

#  #Loop through both keys and values, by using the items() method:
# for x, y in car.items():
#   print(x,y)

#6. Copy a Dictionary: You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#a. Make a copy of a dictionary with the copy() method:
# car= {
#     "brand":"Mercedes",
#     "model":"G-Wagon",
#     "year":1998,
#     "electric": False
# }
# # car2=car.copy()
# # print(car2)

# #b. Make a copy of a dictionary with the dict() function:
# car2=dict(car)
# print(car2)

#7. Nested Dictionaries: A dictionary can contain dictionaries, this is called nested dictionaries.
# myfamily={
#     "child1":{
#         "name":"zeff",
#         "year":2028
#     },
#     "child2":{
#         "name": "faiz",
#         "year": 2030
#     }
# }
# # print(myfamily)
# #Access Items in Nested Dictionaries: To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# print(myfamily["child1"]["name"])
# print(myfamily["child2"]["year"])

