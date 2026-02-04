#Set is a colecion which is unorder, unchange and unindex and no duplictae member
#is a writen {}

"""#Create a set
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))"""

"""#Empty set
empty_set = set()
print(type(empty_set))"""

#No duplicate valve showing on output
#Indexing not allow to set
#Value can not change in set

#Basic set operation
"""#Adding removing elements

set = {1,2,3,4,5,6}

set.add(7)
print(set)

set.remove(3)
print(set)

#discard
set.discard(11) #11 is no available on set but still its showing outpu thats called discard
print(set)

#pop methods are used to remove an item and return its valve

remove_element = set.pop()
print(remove_element)
print(set)"""

"""#clear methods are used to  clear all elements
my_clear = set.clear()
print(my_clear)
print(set)"""


#set methods
my_set = {1,2,3,4,5}
print(my_set)
print(3 in my_set)
print(10 in my_set)


#Mathematical Operation
"""set1 = {1,2,3,4,5,6,}
set2 = {4,5,6,7,8,9,10}

#Union : combine elements 2 or more set into a single set.
union_set = set1.union(set2)
print(union_set) #show all elements but  any duplicate value show only 1 time,

#Intersection_set

intersection_set = set1.intersection(set2)
print(intersection_set) #show only those element who's present in boh side 


set1.intersection_update(set2)
print(set1)

set2.intersection_update(set1)
print(set2)"""