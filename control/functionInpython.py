#A function is a block of code that perform a specific ask.
#Function help in Organizing code. Reusing code and Improving Readatrility.


#syntax
def function_name(parameters):
    """docstring"""
    #function body
    return Expression  

#why function??
"""num = 24
if num%2==0:

    print("the number is even")
else:
    print("the number is odd")"""


#In Function

def even_or_odd(num):
    """this function find even or odd"""
    """if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
"""
#call this function.
even_or_odd(21)
even_or_odd(1000002)


#function with multiple parameter

"""def add(a,b):
    return a+b
result= add(5,6)
print(result)"""



##default parameter
"""
def greet(name):
    print(f"Hello {name}")
greet("Mohsin")


#default parameter another example

def greet (name = "guest"):
    print(f"{name} welcome to the paradise")
greet("Maha")"""


#Variable enth argument
#posiional and keyword arguments

"""def print_numbers(*args):
    for number in args:
        print(number)
    
print_numbers(1,2,3,4,5,6,7,8,9,"Mohsin")"""


#keywords arguments

"""def print_details(**kwargs):
    for key,valve in kwargs.items():
        print(f"{key} : {valve}")
print_details(name = "dan", age= "21", country = "india")"""


#Args and kwargs

"""def print_details(*args, **kwargs):
    for val in args:
        print(f"positional argument: {val}")
    for key,values in kwargs.items():
         print(f"{key}:{values}")

print_details(1,2,3,4,5,"Mohsin",name = "dan", age= "21", country = "india")
"""


#Return Statement
"""
def multiply(a,b):
    return a*b

print(multiply(9,9))"""


# video 23 More example 

#temperature Conversion
def convert_temperature(temp, unit):
    """this function convert temperaure between cel and Fahrenheit"""
    if unit == "C":
        return temp * 9/5 + 32 #cel to F
    elif unit == "F":
        return (temp - 32)*5/9 #F to cel
    else:
        return None

print(convert_temperature(5, "C"))
print(convert_temperature(85, "F"))
print(convert_temperature(800, "C"))
print(convert_temperature(800, "F"))
print(convert_temperature(1, "F"))
print(convert_temperature(1, "C"))



# password Strength checker

def is_strong_password(password):
    """this is strong password  if password is strong or not"""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*+*/-' for char in password):
        return False
    return True


print(is_strong_password("weekend@123"))
print(is_strong_password("Str0ngPWd1123!)"))