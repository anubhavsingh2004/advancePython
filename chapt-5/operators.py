# operators in py

#1 arithm operators:
a=5
b=6
print("add:",a+b)
print("mult;",a*b)
print("div:",a/b)
print("floor div:",a//b)
print("expo:",a**b)
print("mod:",a%b)

#2 comparision operator
#o/p gives boolen value 
print("greater than :", a>b)
print("less than :", a<b)
print("equal :", a==b)
print("greater than  equal to :", a>=b)
print("not equal to :", a!=b)

#3 assignment operator
# a = 5 is an assign operator
# a+=5

#4 logical operator
#1 AND 
# rule for AND operator: T+T=T, T+F=F, F+F=F
A, B = 10, 20
print("and operator:",A>15 and B<10)#F+F=F
print("and operator:",A>8 and B<12)#T+F=F
print("and operator:",A>8 and B<21)#T+T=T

#2 OR 
#RULES FOR OR OPERATOR: T+F=T, T+T= T, F+F=F
print("or operator:",A>8 or B<10)#T+F=T

#3NOT 
#RULES FOR NOT OPERATOR: (and ka ulta) T+T=F, T+F=t
print("not operator:",not(A>8 and B<21))#T+T=T->F

#5identity operator - is , is not 
#gives o/p based on storeage location and not on value
x=[1,2,3]
y=x
z=[1,2,3]
print("x is y:",x is y)#not coz of value but for location same
print("x is z:",x is z)# value me to same, but z is stored else and x also


#6 membership operator
#rules for in operator: agar list me value hai to T warna false
#rules for not in operator:agar list me value hai to F warna true
my_list=["apple", "banana","grape"]
print("apple in my_list: ", "apple" in my_list)

#7 bitwise opertor: considers nums in binary 
#and: cmpares binary AND and gives num in result
a,b=5,3 # 5 in bin is 0101 and 3 in bin is 0011
print("a&b:",a&b)#=>and opertn of each bit gives 0001=>1
print("a|b:",a|b)