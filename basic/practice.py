"""Dictionaries: - dict are unorder and changeble and do not alow dublicate
                dict is a used to store data valves in key: valve pair
                python 3.7 dicts in order
                python 3.6 dicts in unordered
                It is writen {}"""

"""#Creating Dict
empty_dict={}
print(type(empty_dict))

#OR

empty_dicts = dict()
print(type(empty_dicts)) """   


"""student = {"name": "Mohsin", "age": 34, "grade": "A"}
print(student)
print(type(student))"""

"""#single key is always used
student = {"name": "Mohsin", "age": 34, "age": "33"}
print(student)"""

#Accessing Dict elements

student = {"name": "Mohsin", "age": 34, "grade": "A"}

"""print(student["grade"])
print(student["name"])
print(student["age"])"""

#Accessing using get method.

"""print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name', "Not available"))"""

#modifying dict element :- dict are mutable so u can add, update, or delet element

"""#Update
student["age"] = 39
print(student)

#add
student["address"] = "India"
print(student)

#delet
del student["grade"]
print(student)"""


#dictonary Methods
#keys
"""keys = student.keys()
print(keys)

#values
values = student.values()
print(values)

#items
items = student.items()
print(items)"""

