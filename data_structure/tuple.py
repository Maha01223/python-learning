#Tuple
#tupe are order colection of iems tha are immuable they are similar to list,bu their immuable make hem different

#tuple are used o sore mutiple iem in a single variable and its a collection which is ordered and unchange.

#creating empty tuple

"""empty_tuple = ()
print(type(empty_tuple))

lst = list()
print(type(lst))

tuple = tuple()
print(type(tuple))"""

"""mix = [(3.14, True, "hello", 10)]
print(type(mix))
print(mix)"""


#Accessing tuple elements
number = [1,2,3,4,5,6]
#print(number)
"""print(number[0])
print(number[0:3])
print(number[:-1])
print(number[::-1])"""

#Tuple operaions
"""concat = number + mix
print(concat)

print(mix*3) #it mean the  whole list repet in 3 time.
print(number*3)"""

#Immutable Nature of uple
#tuple are immutable a meaning their elements can not be changed once assigned
num = tuple(number)
print(type(num))
number[1] = "krishna"
print(num)
print(number)

#Tuple method
print(number.count(1))
print(number.index(6))


#Packing & unpacing tuple 
#packing
packed_tuple = 1, "hello", 3.14
print(packed_tuple)
print(type(packed_tuple))

#Unpacking
a,b,c = packed_tuple
print(a)
print(b)
print(c)

#one more example
first, *middle, last = number
print(middle)

#Nested Tuple
#Nested list

lst =[[1,2,3,4],[5,6,7,8,9], [10,11,12,13],[14,15,16,17]]
print(lst[2][0])

#iterating over nesed tuple
for sub_tuple in nested_tuples:
    for item in sub_tuples:
        print(item, end='')
    print()