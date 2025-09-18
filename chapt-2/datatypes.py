 #data types in py 
'''a= 1
b=2
print (a+b)
print(type(a))

c='5'
d='2'
print(c+d)
print(type(c+d))
'''
age=20
age_type=type(age)
print("type of age:",age_type)#int

salary= 1.5000
print("type of salary:", type(salary))#float

cordinates= complex(3,6)
print("type of coordinates:", type(cordinates))#complex

name= "anubhav"
print ("type of name:", type(name))#str

lang=['c', 'c++', 'java' , 'py', 5]
print("type of lang:", type(lang))#list

lang1=('c', 'c++', 'java' , 'py', 5)
print("type of lang1:", type(lang1))#tuple

lang_set={'c', 'c++', 'java' , 'py', 5}
print("type of lang_set:", type(lang_set))#set

lang_dict={"sem1":"c", "sem2":"c++", "sem4":"py"}
print("type of lang_dict is:", type(lang_dict))#dict

is_adult=True
print("type of is_adult is:",type (is_adult))#bool