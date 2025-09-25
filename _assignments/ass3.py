#WAP to determine if a given year is a leap year or not

# correct logic is 
# leap year- if year is div by 4
# year is not leap if it is div by 100 unless it is also div by 400
year=int(input("enter a year to check:"))
if year%4==0 and year%100!=0:
    print(f"{year} is a leap year")
elif  year%100==0 and year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")

# option 2
yr=int(input("enter a year:"))
if yr%4==0:
    if yr%100 and yr%400:
        print(f"{yr}is a leap year")
    else:
        print(f"{yr} is not leap")
else:
    print(f"{yr} is not leap")

#approach 3: more optimized

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Q2: login auth using conditional statement
#assume you have predefined username and pass
#both username and pass are correct
#username correct but pass incorrect
#username incorrect.
predefined_username="anubhav"
predefined_passwd='anubhav@1234'
username=input("Enter your username:")
passwd=input("Enter your password:")
if username==predefined_username and passwd== predefined_passwd:
    print("both username and pass are correct\nLogin successfull!!")
elif username==predefined_username and passwd!=predefined_passwd:
    print("username correct but pass incorrect\nLogin Failed!!")
else:
    print("username is incorrect\nLogin Failed!!")


#Q3 admission eligibility, 
# maths>=65,phy>=55, chem>=50
# totak marks in these three>=180 or total maths+phy>=140
m=int(input("enter your maths marks:"))
p=int(input("enter your phy marks:"))
c=int(input("enter your chem marks:"))
total=(p+c+m)
if ((m>=65 and p>=55 and c >=50) and total>=180) or (p+m>=140):
    print("Congratulations!, you're eligible")
else:
    print("Unfortunately You're not eligible")

