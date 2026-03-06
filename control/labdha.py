#Lamdha function
    # lamdha function are small function anonymous function defined using the lamdha keyword.
#The can have any number of argument but only ane expression, 
    #the commonly used for short opeation or as argumnent to high order function.

#syntax
"""lambda argumnets : expression"""

#Basic function
def add(a,b):
    return a+b

print(add(10,20))

#lamdha function

adding = lambda a,b : a+b

print(adding(10,105))



#another example

def even(num):
    if num%2==0:
        return True

print(even(1011))

#lamdha 
even1 = lambda num: num%2==0

print(even1(12))


#multiple  
def addition (x,y,z):
    return x+y+z

print(addition(10,45,85))


#multiple function in lamdha

addition1 = lambda x,y,z : x+y+z

print(addition1(15,85,4595844))




