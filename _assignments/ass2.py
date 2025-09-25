 
#program to take user name and marks of 3 sub and print percentage
name=input("enter your name:")
phy=int(input("Enter your marks in phy:"))
chem=int(input("Enter your marks in chem:"))
maths=int(input("Enter your marks in maths:"))
percentage=((phy+chem+maths)/300)*100
print(f"Hello, {name} your marks are {phy},{chem}, {maths}and your percentage is {percentage}%.")

# Write a programme that collects multiple types of data to store in a dictionary and prints output

#inilizing a dictionary
user_data={}
#take input from user and store it in a dictictionary
user_data['name ']= input("enter your name")
user_data['age ']= int(input("enter your age"))
user_data['height ']= float(input("enter your height"))
user_data['student']= input("enter are you student (Y/N)")
#print user data
print(user_data)
# output:  {'name ': 'anubhav', 'age ': 20, 'height ': 171.0, 'student': 'y'}