#Basic map
# Map Applie a function to all in a list

number =[ 1,2,3,4,5,6,7,8]
def square(number):
    return number*2

print(square(8)) # single Value only


#lamdha function
print(list(map((lambda x: x**2), number)))



# The map function in python
# the map function applie a give function to all items in an input list (or any iterator) 
# this is particular useful for transforming data in a list comprehensively

#normal function
def square(x):
    return x*x

print(square(10))

#In map function

numbers = [11,12,13,14,1,5,1,6,1,7,1,5]
print(list(map(square, numbers)))


#lamdha function with map
print(list(map(lambda x: x*x, numbers)))

#map multiple iterable

number1 = [1,2,3,4]
number2 = [5,6,7,8]

add_number = list(map(lambda x,y:x+y, number1,number2)) 

print(add_number)
