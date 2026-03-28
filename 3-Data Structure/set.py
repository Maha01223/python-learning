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
"""my_set = {1,2,3,4,5}
print(my_set)
print(3 in my_set)
print(10 in my_set)"""


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


#difference

set1 = {1,2,3,4,5,6,7,8,9}
set2 ={4,5,6,7,8,9}
"""#it means set1 ke jo set2 me nahi hai vo he show hoge.
print(set1.difference(set2))
#output {1,2,3}


#symmetric differenec
#it means set1 ke jo set2 me same element hai vo show nahi hoge
print(set1.symmetric_difference(set2))"""


"""#issupsets
print(set1.issubset(set2)) #set1 ke sare elements set2 me hai to he true show hoga otherwise false.

#issuperset
print(set1.issuperset(set2)) #set2 ke saare elements set1 me show hoge to he true show hoga otherwise false

#disjoints
print(set1.isdisjoint(set2)) #agar set1 me aur set2 me koi bhe valve same milege toh false hoga."""

#list convert into set
lst = [1,2,3,3,4,4,5,6,7,8,9,9]
print(set(lst))

#counting unique word in text
txt = "In his tutirial we are discusing"
word = txt.split()

#conver ist of word to set to get unique words
unique = set(word)
print(unique)
print(len(unique))