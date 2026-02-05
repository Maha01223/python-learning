#data structure
#List are ordered, changable allow duplictae member and  mutable colection of items they can contain item of different data types 

#empy list
"""lst = []
print(type(lst))

names = ["Mohsin", "jack", "jacob", 1,2,3,4]
print(names)

mixes = ["mohsin", 1, 3.14, True]
print(mixes)"""


#Accessing List elements

fruits = ["apple", "banana", "cherry", "kiwi", "gauva"]

"""#find fruits index
print(fruits[0])
print(fruits[2])
print(fruits[3])
print(fruits[4])"""


#find all fruis
"""print(fruits[0:])
print(fruits[1:])
print(fruits[-1:])
print(fruits[:2])"""


#medifying the list elemens

"""print(fruits)
fruits[1]= 'watermelon'
print(fruits)

fruits[1:]= 'watermelon'
print(fruits)"""

#List Methods

"""fruits.append("mango")
print(fruits)

fruits.insert(6,'pineapple')
print(fruits)
fruits.extend([101,102,103,104,105,106,107])
print(fruits)"""

#indexing 
index =fruits.index("cherry")
print(index)

print(fruits)


#Remove
"""fruits.pop() #remove last item on the list
print(fruits)

fruits.pop(0) #remove zero index item on the list
print(fruits)

fruits.remove(101) #remove a perticular item on the list
print(fruits)

#fruits.clear() #remove all the items on the list
print(fruits)

new_list= fruits.pop(4)
print(new_list)"""


Branch = ['a','b','c','d','e','f','g','a']

"""print('a' in Branch)
print(Branch.count('a'))


#print(Branch)
#Branch.sort() #sort means the iem of the list change our original place
print(Branch)

new_banch = Branch[:]
print(new_banch)

#new_banch.sort()
print(new_banch)
#sort or sorted both are same
print(sorted(Branch))

Branch.reverse()
print(Branch)

Branch [:] = Branch.copy() #both are right to copy
print(len(Branch))"""

sentence = ' '
"""
new_sentence = sentence.join(['Hello']) #
#new_sentence = ' '.join([Hello])  boh are same working

print(new_sentence)
"""
# list unpacking 
"""a,b,c = [-1,2,3]
print(a)
print(b)
print(c)

a,b,c, * other,d = [1,2,3,4,5,6,7,8,9]

print(other)
print(d)"""

#None is a special ype of data
"""
weapone = None
print(weapone)"""





