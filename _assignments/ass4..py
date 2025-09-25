# Q1 extract the chars from index 2 to 8 at step of 2
my_string="Python Course"
print(my_string[2:9:2])

#Q2 remove the first 3 and last 3 chars from the string
mystring2="Regression Analysis"
result1=mystring2[3:-3]
print(result1)

#Q3 get the substrin that starts from the 4 chars at the end to the last
my_string3="Classification"
print(my_string3[-4:])

#Q4 write a py fn to chk if sting is palindrome or not using str metods 
def palindrome(string4):
    
    return string4 == string4[::-1]
string4=input("enter a string:")
result=palindrome(string4)
print(result)

#Q5 slice to get only the middle chars:


my_string5 = input("enter a string:")
def middle(my_string5):
    length = len(my_string5)
    print(length)
    if length % 2 == 0:
        mid = length // 2
        middle_char = my_string5[mid-1:mid+1]  # two middle characters
    else:
        mid = length // 2
        middle_char = my_string5[mid]  # single middle character
    return middle_char

result5 = middle(my_string5)
print(result5)

'''
my_string5="Madhav"
def middle(my_string5):
    print(len(my_string5))
    if len(my_string5)%2==0:
        middle_char=my_string5[(len(my_string5)/2):((len(my_string5)/2)+1)]
    else:
        middle_char=my_string5[(len(my_string5)/2):(len(my_string5)/2)]
    return middle_char
result5=middle(my_string5)
print(result5)
'''