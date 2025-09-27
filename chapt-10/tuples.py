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