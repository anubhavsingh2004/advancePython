'''Q1 WAP to print folllowing text as it appears- 
Python is fun.
"Quotes" and 'single quotes' can be tricky.
'''
print("Python is fun.")
print('''"Quotes" and 'single quotes' can be tricky.''')

#approach 2: using just one print fn , making the sol more optimized
print('''Python is fun.\n"Quotes" and 'single quotes' can be tricky.''')

'''Q2 for a business create 3 var to store name age and city,
then print a senetence that uses these vars'''

name="Vanmali"
age=21
city="chembur"
print(name, "lives in:", city, "and is",age ,"years old")

#approch 2: using f-strings , more optimzed
name="Vanmali"
age=21
city="chembur"
print(f"{name} lives in: {city} and is {age} years old")