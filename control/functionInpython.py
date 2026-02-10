#A function is a block of code that perform a specific ask.
#Function help in Organizing code. Reusing code and Improving Readatrility.


#syntax
def function_name(parameters):
    """docstring"""
    #function body
    return Expression  

#why function??
num = 24
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")


#In Function

def even_or_odd(num):
    """this function find even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

#call this function.
even_or_odd(21)
even_or_odd(1000002)


#function with multiple parameter

def add(a,b):
    return a+b
result= add(5,6)
print(result)



##default parameter

def greet(name):
    print(f"Hello {name}")
greet("Mohsin")


#default parameter another example

def greet (name = "guest"):
    print(f"{name} welcome to the paradise")
greet("Maha")