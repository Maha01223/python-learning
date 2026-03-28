# print("mohsin")
# print(type(20 + 4))
# print(20 -1)

"""# name = input ("what is your name?")
# print('heelloooooo ' + name)"""

# ------------------Fundamental Date types

# int
# float
# complex 
# bool
# string
# list
# tuple
# set
# dict

"""print(type(21 / 4))
# float
print(type(10 + 2))
# int"""

# -----------------maths Function

"""print(round(3.45))
# output 3
print(round(3.87))
# output 4
print(abs(-25))
# output 25"""

# -----------Operators Precedence

# rules
# ()
# **
# / & *
# + & -

"""print(20 -3 * 4)
# output 8
print((20-5) * 20 / 8)
# output 37.5
print((20**4) / 2 ** 28 + 25 * 4 / 1)
# output 100.00059604
print(8 ** 16)"""

# -----------------------complex number

"""print(bin(32))
# outpu 0b100000
print(int('0b100000', 2))
# output 32"""

# ----------------Variables

# snake_case
# start with lowercase or underscore
# letter , number , underscores
# case sensitive
# don't overwrite keywords
"""print = 190 

print(print)

iq = 167
user_age = iq / 3
a = user_age
print(a)

a,b,c = 1,2,3
print(a)
print(b)
print(c)"""


#  ---------------------Expressions Vs statements

"""iq = 150
user_age = 180 / 5

# 180 / 5 is a Expressions

# user_age = 180 / 5 is a statements"""

# ----------------Augmented assignment operator

"""some_valve = 5
some_valve = some_valve + 2
print(some_valve)
# output 7

# some_valve = 5
# some_valve += 3
# some_valve -=5
# some_valve *= 6
some_valve /= 3
print(some_valve)
# output 8"""

# -----------------Sting---------

"""print(type('heeellllooooooooo this 24!'))

username = 'supercoder'
password = 'supersecret'

long_string = '''
WOW
0 0
---
'''
print(long_string)


first_name = 'Mohsin'
last_name = 'Ansari'
full_name = first_name + ' ' + last_name
print(full_name)"""


# -------------------------String Concatenation---

"""print('hello' + ' Mohsin')
# output helo Mohsin
print('hello' + 5)
# can only concatenate str (not "int") to str

# its work only with strings"""

#-------------------- types of conversion


# print(type(int(str(100))))

"""a = str(100)
b = int (a)
c = type(b)
print(c)"""

# --------------------Excape sequence

"""weaher = "hello 'he\nworld"
# \n means go to new line
print(weaher)

print("hello the way is \"good\" for \na man and give \'good\' way to resolve")

print("eprate", 7 ,8, 10, sep="~")
# sep="~" it means it took a sepration for all valves.
#  output :- eprate~7~8~10

print("eprate", 7 ,8, 10, end="009")
print("harry")"""
 
# Formatted strings

name = ' jonny'
age = 55

# print('hi ' + name + '. you are' + str(age) + ' years old')
# its a old way
# print(f'hi {name}. you are {age} years old')
# f is a formatted strings
# another way
# print('hi {} you are {} years old'.format('mohsin', '55'))

# print('hi {} you are {} years old'.format(name, age, ''))

# print('hi {new_name} you are {new_age} years old'.format(new_name = 'DON', new_age = 100))

# --------------------string index

"""selfish = '01234567'
        #    01234567
# [start : stop : stepover]
print(selfish[0:9:2])
# print(selfish[1:]) #1234567
# print(selfish[:-2])
# print(selfish[:: -2]) #7531"""

# -----------Immutability string------ change na kr pana
# /create string or delect  string but never change

"""selfish ='012345678'

# selfish [0]= '2'
# 'str' object does not support item assignment

selfish2 = selfish + '9'

print(selfish)
print(selfish2)
# output :- 0123456789"""


# ---function are two type---------
# Buit_In Function +.
# Methods. and user define function
 
"""a = 9
b = 8
gmean1 = (a-b)/(a+b)
print(gmean1)

c = 8
d = 7
gmean2 = (c-d)/(c+d)
print(gmean2)"""


"""
def calculateGmean(a, b):
    mean = (a-b)/(a+b)
    print(mean)
    

def managerWord(a,b):
    if(a>b):
        print("yes")
    else:
        print("no")
        
def islessthan (a,b):
    pass

# a = 9
# b = 8
# # gmean1 = (a-b)/(a+b)
# # print(gmean1)
# calculateGmean(a, b)

# c = 8
# d = 7
# # gmean2 = (c-d)/(c+d)
# # print(gmean2)
# calculateGmean(c, d)



a = 9
b = 8

if(a>b):
    print("yes")
else:
    print("no")
    
calculateGmean(a, b)
    
c = 2
d = 3

managerWord(c,d)
calculateGmean(c, d)"""

# build in function

"""quet = 'to be or not to be'

# print(quet.upper())
# print(quet.capitalize())
# print(quet.find('be'))
# print(quet.replace('be','me'))
quet2 = quet.replace("be", "me")
print(quet2)

print(quet)


# print(len(quet))

print(len('helllo'))

greet = 'helllo'
print(greet[0:len(greet)])"""


# -----------calculater

"""number1 =int(input("enter the valve of first no. = "))
number2 =int(input("enter the valve of second no. = "))

add = number1 + number2
print("the sum of", number1, " and ", number2, "is", add)

sub = number1 - number2
print("the sum of", number1, " and ", number2, "is", sub)

mul = number1 * number2
print("the sum of", number1, " and ", number2, "is", mul)

div = number1 / number2
print("the sum of", number1, " and ", number2, "is", div)"""

# ------boolean---

# name = 'andew'
is_cool = False
is_cool = True

# print(bool())


# -----excercise type

"""name = 'Mohsin Ansari'
age = 26
relationship_status = 'single'
relationship_status = 'it\'s complicated'
# print(relationship_status)

# ----

birth_year = input('what year were you born?')
# print(type(birth_year))

age = 2023 - int(birth_year)

print(f'your age is :{age}')"""


# ------------password hidden

"""username = input('what is your username?')
password = input('what is your password?')

password_length = len(password)
hidden_password = ('*' * password_length)

print(f'hey {username}, your password {hidden_password} is {password_length} letter longs')

# print('*' * 10) hidden way"""

# -----------List--------


# List is a collection which is ordered and changeable. Allows duplicate members.
# list is in  any think like float,int,str,bool anything
# its look like javascript arry. 

"""a = [1,2,3,4,5]
b = ['abbas','daaaaaaan','sparsh']
c = [1, 'john', True, 2.5]

print(a[1])
print(b[2])
print(c[2])
"""
# -----------List slicing
# string is immutability it means you can not replace any other items on string but you create new string.

"""string = 'helloooo'
print(string[0:4:2])
string[0] = 'z' #TypeError: 'str' object does not support item assignment"""


#  but in list you can change iteams so its a mutabile

"""amazon_cart= [
        'notebooks',
         'sunglasses',
         'toys',
         'grapes',
]

amazon_cart [0] = 'laptop' #like that
# new_cart = amazon_cart[0:3]
new_cart = amazon_cart[:] #with out [:] its can not give orignal amazon_chat.
# new_cart[0] = 'gum'
# new_cart[1]= True
# print(new_cart)
# print(amazon_cart)"""

"""# example 
new_list = ['a', 'b', 'c']
print(new_list[1]) #b
print(new_list[-2]) #a
print(new_list[1:3]) #bc

new_list[0] ='z'
print(new_list) #zbc

my_list =[1,2,3,4]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

my_list = [1,2,3,4,5,6]
print(my_list[-5])"""

# ----Matrix-----

"""matrix = [
    [1,5,[1,5,6]],
    [1,2,1],
    [0,6,1],
    [9,8,7]
]

print(matrix[0][2][0])"""

# method

# basket = [1,2,3,4,5,6]
# adding

# new_list = basket.append(100) its showing none because first you append the item then create new list. 
# print(new_list)
# print(basket) 
#  print(basket)

# basket.append(100) #add this item on last list 
# basket.insert(4, 200)
# basket.extend([101,200,3000])
# new_list = basket
# print(new_list)

# removing
# basket.pop() #in here its remove end of the list items.
# basket.pop(0) #in there its remove according to  index item.
# basket.remove(3) its remove items of list according a name 
# new_li = basket.pop(4)
# basket.clear()
# new_li = basket
# print(new_li)
# print(basket)
 
basket = ['a','x', 'b', 'c', 'd', 'e', 'f', 'g']

# print(basket.index('d', 0, 3)) check again 
# print('d' in basket) 
# print('x' in basket)

# print(basket.count('d')) #number of a how much in this list to check with count
# print(basket)
# basket.sort()

"""new_basket = basket[:]
new_basket.sort()
print(new_basket)
# =============or
print(sorted(basket)) #shorted is create a new basket ""
print(basket)"""

"""new_basket = basket [:]
print(basket)
# -------O---- both R same
new_basket = basket.copy()
print(basket)

print(len(basket))
print(basket)
basket.sort()
print(basket)
basket.reverse()
print(basket)

print(basket[::-1]) #its working reverse

print(list(range( 100)))"""


# sentence = ' '

"""new_sentence = sentence.join(['hi','my', 'jojo'])
print(new_sentence)

# o----------------OR------------r

new_sentence = ' '.join(['hey', 'my', 'name', 'is', 'JOJO'])

print(new_sentence)"""



# ---------List unpacking

"""a,b,c, * other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)
"""


"""lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

# ------------None
# is a special type of data
weapons = None

print(weapons)"""

#-------------Dictionaries----------is un-order key payers.

"""# dictionary

dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}
print(dictionary['a'][2])
print(dictionary['b'][2])
print(dictionary['x'])

# as a list show how to work

my_list = [{
    'a': [1,2,3],
    'b': 'hello',
    'x': True
},
{
    'a': [4,5,6],
    'b': 'you',
    'x': False
}]

print(my_list[0]['a'][0])
print(my_list[0]['b'][2])
print(my_list[0]['x'])

print(my_list[1]['a'][0])
print(my_list[1]['b'][2])
print(my_list[1]['x'])"""


# Developer fundemental -----extra classes

dictionary = {
    '123' : [1,2,3],
    '123': 'hellloooo',

}

# print(dictionary['123'])
# dic has unique key value. it can not be change key

"""user = {
    'basket' : [1,2,3],
    'greet': 'hellloooo',
    # 'age': '200 '

}
# if there is no age variable to its a default valve to givin
print(user.get('age', 50))

# user2 = dict(key=valve) formula to create dict
user2 = dict(name = 'jon jone')
print(user2)"""



user = {
    'basket' : [1,2,3],
    'greet': 'hellloooo',
    'age': 50

}


# print('basket' in user.keys())
# print('wind' in user.keys())
# print(200 in user.values())

# print(user.clear())
# print(user)

# user2 = user.copy()
# print(user2)

# print(user.items())
# # output comes as a tupples

# print(user.pop('age'))
# # remove that iteam on user
# print(user)

# print(user.popitem())
# print(user)

# print(user.update({'age': 2600}))
# print(user)

# tupple

"""
tup = (1,2,3,2)
print(len(tup))
print(tup.count(2))
print(tup.index(1))"""


# -------------set
# doubelicate valve not allow and indexing not allow

set = {1,2,3,4,6,5} 
set2 = {4,5,6,7,8}
# print(set)
# print(set.union(set2))
# set.update(set2)
# print(set, set2)

# print(set.intersection(set2))
# set.intersection_update(set2)
# print(set)

# print(set.symmetric_difference(set2))
# set.symmetric_difference_update(set2)
# print(set)

# print(set.difference(set2))
# set.difference_update(set2)
# print(set)

# print(set.isdisjoint(set2))

# print(set.issuperset(set2))
# print(set2.issubset(set))

# set.add(100)
# print(set)

# set.update(set2)
# print(set)

# set.discard(1)
# print(set)

# print(set)

# print(set[0])
# TypeError: 'set' object is not subscriptable

# print(len(set))
# new_se = set.copy()
# print(new_se)
# new_se =set.clear()
# print(new_se)
# print(set)
# print(set.add(12))
# print(set)
# set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,12}

# print(set.difference(your_set))
# {1, 2, 3}

# print(set.discard(5))
# # remove that item
# print(set)

# print(set.union(your_set)) both doing same work # print(set | your_set)


# print(set.difference_update(your_set))
# print(set)

# print(set.intersection(your_set)) both doing same work  # print(set & your_set)
# {4, 5}
# print(set.isdisjoint(your_set))


# set = {4,5}
# your_set = {4,5,6,7,8,9,12}
# print(set.issubset(your_set))
# print(set.issuperset(your_set))














