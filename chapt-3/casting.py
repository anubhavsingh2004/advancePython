'''a=1
print(type(a))

a1='11'
print(type(a1))

b=int(a1)
print(type(b))

mynum=25
mynum2=str(mynum)
print(type(mynum2))

f1=56.23
print(type(f1))

f2=(int(f1))
print(f"the value {f1} with type {type(f1)} in int datatype is {f2} with type {type(f2)}")

x1= 1929
x2=float(x1)
print(f"the value {x1} in float is {x2}")# by default gives one zero after decimal point
'''

#implicit type casting
var1= 10
var2=10.5
var3=var1+var2
print (f"{var3}, {type(var3)}")