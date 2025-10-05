#Tuples in python:
 
my_tuple=(1,2,3,4)
print(my_tuple)

#methods to create tuples:

#1 using parenthesis:
my_tuple=(1,2,3,4)

#2 without parenthesis:
tuples1=1,4,6,3 # it is also a tuple
print(tuples1)

#3 using tuple constructor:
helllo=tuple((2,5,"hii")) #should have double()
print(type(helllo)) 
list3=[4,5,6,8]
list_tuple=tuple(list3)
print(list_tuple)

#4 creating a single element tuple:
a=("a",)       # a comma after the elemt is must
print(type(a)) # otherwise it will the elem as a str


#accesing the elem of a tuple
# by indexing:
 
new_tuple=("a","c","d")
print(new_tuple[1])

#tuple slicing:
#accesing a range of elemts in tuple
new_tuple=("a","c","d", "e", "a")
print(new_tuple[1:4])

#tuple operations:
#1 conctenation:
tup1=(1,2,3,5)
tup2=(6,7,8)
combined=tup1 +tup2
print(combined)

#2 repetition;
tup3=(1,2,34)*3
print(tup3) # print three times in the same list

#3 checking for elem in tuple:
tup4=(1,2,34,6,7)
print(7 in tup4)   #returns T/F

# tuple methods:
# python only has two built in mtheods - count , index()
colors=(1,2,4,2)
print(colors.count(2))
print(colors.index(2)) #pehla occurance of 2 ka index dega

# tuple functions:
# len(),
#  sorted()- sorts the tuple but returns a list,
#  sum()- returns the numeric sum
# min, max()

print(len(colors))
print(sum(colors))
print(sorted(colors)) #returns a list sorted
print(min(colors)) 

# packing and unpackin a tuple:

# packing- putting multiple values into a single tuple 
# unpacking is extractings values from a tuple into seperate variables

# modifying tuples:
# once a tuple is created you cannot modify it, as it is/
# immutable so what is its use?- used in areas where the
#  values are not expected to chnge like lats longs of earth

# but if really want to modify the tuple we can convert it to
#  lst instead before changing and then after we are done modifying
#  the list we can chng it back to tuple
 #ex 
numbers45=1.2,5,86,9
print(type(numbers45))
numbers45_list=list(numbers45)
numbers45_list[2]=45
print(numbers45_list)
numbers45=tuple(numbers45_list)
print(numbers45)