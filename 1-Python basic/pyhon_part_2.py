# conditional logic

"""is_old = True

is_licenced = True

if is_old:
    print("your age is eleigible")
elif is_licenced:
    print("now you drive")



if is_old and is_licenced:
    print("your age is eleigible")  

else:
    print("dont alow o dirve")

print('okoko')"""




# truthy and falsy
"""is_a = bool(('hello'))
is_b = (5)
print(is_a)

# truthy
print(bool('hello'))
print(bool(5))

# falsy
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool(None))"""



"""password = bool("123")
username = " Jonnny"
print(type(password))

if password and username:
    print("okkky")
else:
    print("nonono")"""



# ternary Operator and conditional  expression

"""# condition_if_true if condition else condition_if_false

is_friend = True
can_messgae = "mesage allows" if is_friend else "not allowed to message"

print(can_messgae)"""



# Short circuiting
"""
is_friend = True
is_users = False

if is_friend and is_users: 
# #dono valve true hoge tab print hoga.
    print('best friend forever')

if is_friend or is_users: 
# #or me ek bhe valve true hoge tohbprint hoga.
    print('best friend forever')"""


  # logical operators

#  >, <, >=, <=, ==, != and or not
a = 17
# print(a > 18)
# print(a < 18)
# print(a >= 18)
# print(a <= 18)
# print(a != 18)
# print(not(False))
# print(not(True))
# print(not(1 == 1))
# print(not(1 != 1))



# exercise 

"""is_magician = True

is_expert = False

# check if magician AND expert: print("you are a master  magician")

if is_magician and is_expert:
    print("you are a master  magician")

elif is_magician and not  is_expert:
    print("at least you are getting here")

elif not is_magician:
    print("you need magic power")"""


# IS VS ==

# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])
# print({} == [])


# print(True is 1)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])
# print({} is [])


# Loops is a list, dic, set, tuple

# for variable in 'zero to mastery':
#     print(variable)

# for variable in [1,2,3,4,5,6,6]:
#    for x in  ['a', 'b', 'c', '4']:
#     print(variable, x)


# Iterable - is a list,set,dic, tuple, string
# iterate means one-by-one check each item in the collection.

"""user = {
  'name' : 'Mohsin',
  'age' : 506,
  'swim' : False
} 
for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for item in user.items():
   print(item)

for item in user.items():
  key, valve = item;
  print(key, valve)

  OR both are same

for key, valve in user.items():
#   key, valve = item;
  print(key, valve)"""


"""execise

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
  counter = counter + item
  print(counter)"""

# # ------------------range

"""print(range(100))
# assending
for number in range(0, 10):
    print(number)

# decending
for _ in range(10, 0 , -1):
    print(_)


for _ in range(2):
    print(list(range(1, 9)))"""

 
# while loops
"""i = 0
while i < 5:
    print(i)
    i = i + 1
    # i += 1
    # break
else:
    print("done all he work")"""

# # for loop

"""my_list = [1,2,3,4,5,6]
for item in my_list:
    print(item)"""

"""i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
"""

"""while True:
   response =  input("say same thing: ")
   if (response == 'bye'):
    break"""
    
# Enumerate()

"""for i,char in enumerate('hellooo'):
    print(i, char)

for i,char in enumerate(list(range(1, 100))):
  print(i, char)

for i,char in enumerate(list(range(1, 100))):
  print(i, char)
  if char == 50:
    print(f'index of 50 is: {i}')"""
    
    
    
# Excercise  
# clean code 
# readibility
# predictability
# DRY

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

"""# 1 iterate over picture
# if  0 -> print ''
# if 1 -> print *"""
"""
for row in picture:
    for pixel in row:
        if(pixel == 1):
            print('*',end= ' ')
        else:
            print(' ', end= ' ')
    print('')
# # or



# empty = ' '
# fill = '*'

# for row in picture:
#     for pixel in row:
#         if(pixel):
#             print(fill, end= '')
#         else:
#             print(empty, end= '')
#     print('')"""

# Excercise: Check for duplicate  in List:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

"""# A set to keep track of elements that have been seen
seen = set()
# A list to store duplicates found in the input list
duplicates = []

# Iterate over each element in the list
for i in some_list:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)


# both are doing same work 

# duplicate = []
# def show_tree():
#     for valve in some_list:
#         if some_list.count(valve) > 1:
#             if valve not in duplicate:
#                 duplicate.append(valve)
#     print(duplicate)

# show_tree()"""

# function

"""# def say_hello():
#     print('helllloooo')

# say_hello()


# Argument and parameters

# positional parameter
# parameter are use to define to the function
# DEFAULT PARAMETER
def say_hello(name= 'Dan', emoji= '👺'):
    print(f'hello {name}{emoji}')
    
# say_hello()
# say_hello('timmy')
    
# argument are used to call to  the function
# positional Arguments
say_hello('mohsin', '🥹')
say_hello('🤩', 'mohsin')
say_hello('mohsin', '🥹')


# keywords arguments

# say_hello(emoji='🥹', name= 'Bibi')
# say_hello(name= 'Bibi', emoji='🥹')"""



# return
# should do one thing really well.
# should return something.

"""def sum(num1, num2):
    add = num1 + num2
    print(add)
    
num1 = 10
num2 = 20
 
sum(num1, num2)
sum(15, 10)"""

    # ORRRRRR
    
"""def sum(num1, num2):
    return num1 + num2


num1 = 10
num2 = 20

total = sum(10, 15)
print(sum(num1, total))

# say another way
print(sum(10,sum(10, 15)))"""


# complex return valve 

"""
def sum(num1, num2):
    def another_function(n1, n2):
        return n1 + n2
    return another_function(num1, num2)

total = sum(10, 25)
print(total)"""


# exercise
"""age = input("what is yor age?: ")

if int(age) < 18:
    print("sorry ,you are not eligible")
elif int(age) > 18:
    print("power On enjoy the ride!")
elif int(age) == 18:
    print("congratulation")"""
    
    
# excercise

"""def checkDricerAge():
        age = input("what is your age?: ")
        if int(age) < 18:
            print("sorry ,you are not eligible")
        elif int(age) > 18:
            print("power On enjoy the ride!")
        elif int(age) == 18:
            print("congratulation")
checkDricerAge()"""

# Methods VS Functions

# function
"""Function is block of code that is also called by its name. (independent)
The function can have different parameters or may not have any at all.
If any data (parameters) are passed, they are passed explicitly.
It may or may not return any data.
Function does not deal with Class and its instance concept."""

# list()
# print()
# max()
# min()
# input()

"""def Subtract (a, b):
	return (a-b)

print( Subtract(10, 12) ) # prints -2

print( Subtract(15, 6) ) # prints 9


def some_random_suff():
    pass
"""
# methods
"""Method is called by its name, but it is associated to an object (dependent).
A method definition always includes ‘self’ as its first parameter.
A method is implicitly passed to the object on which it is invoked.
It may or may not return any data.
A method can operate on the data (instance variables) that is contained by the corresponding class"""

# Python 3 User-Defined Method
"""class ABC :
	def method_abc (self):
		print("I am in method_abc of ABC class. ")

class_ref = ABC() # object of ABC class
class_ref.method_abc()"""


# docstring imp 
"""def test(a):
    '''
    info: its a doc string to print a
    '''
    print(a)
    """
# test('!!!!!')

# help(test)
# print(test.__doc__)

# clean code

"""def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
    
    # or
    
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
    # or
    
def is_even(num):
    if num % 2 == 0:
        return True
    return False

# OR

def is_even(num):
    return num % 2 == 0


print(is_even(101))"""

# *Arg is a tuple and **kwargs is a dict
# **args

# def auper_func(*args):
#     print(args)
#     return sum(args)
 
# print(auper_func(1,2,3,4,5))

# **kwargs

# def auper_func(*args, **kwargs):
#     print(kwargs)
#     return sum(args)
 
# print(auper_func(1,2,3,4,15, num1=5, num2= 10))


# both
"""
def super_func(*args, **kwargs):
    total =0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1= 5, num2= 10))"""


"""rule: params, **args, default parameters, **kwargs

def super_func(name, *args, i='hi', **kwargs):
    total =0    
    for items in kwargs.values():
        total += items
    return sum(args) + total 

print(super_func('mohsin', 1,2,3,4,5, num1= 5, num2= 10))"""

# Exercise 

def highest_even(li):
    even = []
    for items in li:
        if items % 2 == 0:
            even.append(items)
    return max(even)
    
print(highest_even([10,1,2,3,4,5,6,7,8,9,11,12,91]))