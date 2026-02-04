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

student = {"name": "Mohsin", "age": 28, "grade": "A"}

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
"""#keys
keys = student.keys()
print(keys)

#values
values = student.values()
print(values)

#items
items = student.items()
print(items)"""

#Iterating over dict 
#You can use loops to iterative over dic keys,values or items
"""#iterating over keys
for keys in student.keys():
    print(keys)

#iterating over values
for values in student.values():
    print(values)

#iterate over keys valve pairs
for keys, valves in student.items():
    print(f"{keys}:{values}")"""


#Shallow copy
"""#normal copy
student_copy = student
print(student)
print(student_copy)

#update
student["name"] = "Sparsh"
print(student)
print(student_copy)"""

"""#its a shallow copy
student_copy1 = student.copy()
print(student_copy1)
print(student)

#update

student["name"] = "Abbas"
print(student)
print(student_copy1)"""


#Nested dictionaries

"""students ={
    "student1": {"name": "maha", "age": 28},
    "student2": {"name": "dan", "age": 27}
}

print(students)

#access nested dict elemtnt
print(students["student1"]["name"])
print(students["student2"]["age"])"""


#list example
"""
mylist = [
    {
    'a': [1,2,3],
     'b': 'hello',
     'c': True},
        {
        'a': [4,5,6],
        'b': 'you',
        'c': False}]
print(mylist)
print(type(mylist))

print(mylist[0]['a'][1])"""


#Iterating over nested dictionaries

"""students ={
    "student1": {"name": "maha", "age": 28},
    "student2": {"name": "dan", "age": 27}
}

for student_Id, student_info in students.items():
    print(f"{student_Id}:{student_info}")
    for key,valve in student_info.items():
        print(f"{key}:{valve}")"""


#dictonaries comprehension

"""square = {x:x**2 for x in range(10)}
print(square)

#conditions dict comprehansion

even = {x:x**2 for x in range(10) if x%2==0}
print(even)"""

#use a dict to count he frequency of element in list

"""numbers = [1,2,2,3,3,3,4,4,4,4,5,10,10,10,10]
frequency ={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)"""

#merge two dict
"""dict1 = {'a':1,'b':2}
dict2 = {'b':3, 'c': 4}

merge = {**dict1, **dict2}
print(merge)

keys = dict1.keys()
print(keys)"""


#fundemental 
"""dict = {
    '123': [1,2,3],
    '123': 'hello'
}

print(dict)
#dict has unique key, valve it can not be change key do not overlep"""


user = {
    'basket': [1,2,3,4],
    'greet': 'hello',
    'age': 50
}

print(user)
print(user.keys())
print(user.values())

#find
print('basket' in user.keys())
print('wind' in user.keys())
print(200 in user.items())
print(user.update({'name': "mohsin"}))
print(user)