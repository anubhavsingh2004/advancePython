#functions:
#user def functions:

def greetings():
    print("hello all gm")

#call
greetings()

def add2nums(a,b):
    sum=a+b
    print("addition is :",sum)

add2nums(7,0)
add2nums(b=5, a=9)

#fn with return statement:
def addnum(a,b):
    return a+b
    return a-b #after return statement fn ends
sum=addnum(5,2)
print(sum)

#fn to convert celsius to fahrenheit
def temo_convert(celsius):
    fahrenheit = (celsius*9/5) +32
    return fahrenheit
#call fn
t= temo_convert(51.3)
print(t)


#fn to convert celsius to fahrenheit without return
def temo_convert(celsius):
    fahrenheit = (celsius*9/5) +32
    print(fahrenheit)
#call fn
t= temo_convert(51.3)
print(type(t))#124.34
# <class 'NoneType'> 

#fn to convert celsius to fahrenheit with return
def temo_convert(celsius):
    fahrenheit = (celsius*9/5) +32
    return fahrenheit
#call fn
t= temo_convert(51.3)
print(t,type(t)) #124.34 <class 'float'>

#The Pass statement:
def kuchbhi():
    pass
print("hello")

#HW
# WAP to create a Calculator and perform operations 
def add2num(num1,num2):
        return num1+num2
def sub2num(num1,num2):
        return num1-num2
def mul2num(num1,num2):
        return num1*num2
def div2num(num1,num2):
        return num1/num2
def expo2num(num1,num2):
        return num1**num2

num1=int(input("enter num 1:"))
num2=int(input("enter num 2:"))
print("Enter Your choice: \n \
       choice =1 for addition \n \
        choice =2 for substract \n \
        choice =3 for multiply \n \
        choice =4 for divide \n \
        choice =5 for expoential \n")
choice=int(input("enter your choice:"))
if choice==1:
    print(add2num(num1, num2))
elif choice==2:
    print(sub2num(num1, num2))
elif choice==3:
    print(mul2num(num1, num2))
elif choice==4:
    print(div2num(num1, num2))
elif choice==5:
    print(expo2num(num1, num2))
else:
    print("Enter a valid choice")
