#Basic map
# Map Applie a function to all in a list

number =[ 1,2,3,4,5,6,7,8]
def square(number):
    return number*2

print(square(8)) # single Valve only


#Map function
print(list(map((lambda x: x**2), number)))



# The map function in python
