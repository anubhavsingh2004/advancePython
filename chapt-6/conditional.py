#conditional statements in py

num=int(input("enter a num:"))
if num>0:
    print(f"{num} is positive")
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
else:
    print("num is negative")

#1 if statements:
'''a=5
b=7
##if a<b :
    #print("b is greater tha b")
if a>b :
    print("b is greater tha b")'''

#age=int(input("enter your age:"))
#if age>18:
#    print("you are an adult")

#2 if-else statemnet
#age=int(input("enter your age:"))
#if age>=18:
 #   print("you can vote")
#else:
#    print("you cant vote")

#3 if-elif-else:
#percent=float(input("enter percentage:"))
#if percent>=85:
#    print("Passed with distinction")
#elif percent<=85 and percent >=65:
#    print("passed with first class")
#elif percent<=65 and percent >= 50:
#    print("passed with second class")
#elif percent<=50 and percent >= 35:
#    print("you are just passed")
#else:
#    print("Failed!")


#4 Nested 'if-else':
# ie if else inside another if else
#WAP to classify num as positive or negative and even and even and odd if +ve
n=int(input("enter a num:"))
if n > 0:
    if n%2==0:
        print ("num is positive and even")
    else:
        print("num is positive but odd")
else:
    print("num is negative")


#5 conditional expressions (ternary operator)
age=17
status="adult" if age>=18 else"minor"
print (status)