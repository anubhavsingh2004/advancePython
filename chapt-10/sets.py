# sets in python:

# set is a collection of items in python ,
# the elemts in a set is unique and unrdered 
# and also set is muteable 
# but the elemts in stes are not mutable
# set- unordered, unique, mutable, elements immutable.
# meaning elemts of sets can be added or rm after creation
# but no replacements possible

vowels={'a','e', 'i','o','u'} #set- elemts sep by comma in curly braces

#creating a set:
# two methods: using {}, set() constructor

#1 using curly braces:
myset={1,2,3,4}
print(type(myset), myset)

#2 using the set() constructor:
myset2=set([1,2,34,5])
print(type(myset2), myset2)

# NOTE: we cannot create an empty set using the {}
# as it will create a dict instead
#  to do that we should create a set using the set() constructor.

# set operations:
# add(), and remove methods:
#1 add methods: 
myset3={1,2,5,8}
myset3.add(99) # does not need to specify position coz set is unordered
print(myset3)

#2 remove methods: two- remove(), discard()
myset4={18,88,99,55}
myset4.remove(88)
print(myset4)
# myset4.remove(88) will throw error as remove method throws error if elem is not pr.
myset4.discard(88)
print(myset4)
myset4.discard(18)
print(myset4)

# set functions:
# union, intersection, diff, symm diff

#1 union:
set1={1,2,3}
set2={2,5}
unionset=set1.union(set2)
print(unionset)

#2 intersection:
set1={1,2,3}
set2={2,5}
# interset=set1.intersection(set2)  # method 1
interset= set1 & set2  # method 2
print(interset)

#3 difference :
set1={1,2,3}
set2={2,5}
diffset=set1.difference(set2) #this is set1 - set2
print(diffset)

#4 symmetric difference :
set1={1,2,3}
set2={2,5}
symmset=set1.symmetric_difference(set2) # this is union(set1, set2)- intersection(set1,set2)
print(symmset)

#set iterations:
#for loop:
#3 difference :
set1={1,2,3}
for i in set1:
    print(i)