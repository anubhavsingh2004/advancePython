# Q1 print the while loop output in the same line:
count=0
while count<5:
    print(count, end=" ")# understood that the print fn has three things value, sep, end 
    count+=1

#Q2 print star pattern using loops:
n=5
for i in range (1,n+1):    
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#Q3: WAP to find factorial of a num:
n=5
result=1
while n>0:
    result= result*n
    n-=1    
print(result)

#Q4 WAP to count the num of vowels in a string:
string="my Nmae is Anubhav im am 21"
vowels="aeiou"
count=0
print(len(string))
for char in string:
    if char.lower() in vowels:
        count+=1
print(count)

#Q5 find the longest  word in the sentence using for loop:

def lw(string):
    longest_word=""
    string_word=string.split()
    print(string_word)
    for word in string_word:
        if len(word) > len(longest_word):
            longest_word=word
    return longest_word
print(lw("my Nmae is Anubhav im am 21")) #glt kyu aarha h ye? pta nhi -hogaya sahi yee

#Q6 print fibo series of first n nums using while loop:
n=10
a,b=0,1
while n>0:
    print(a,end=" ")
    a,b=b,a+b
    n-=1

n=10
a,b=0,1
count=0
while count<n:      #sir ka sol
    print(a,end=" ") 
    a,b=b,a+b
    count+=1

text = "hello world"
brokenLetters = "ad"
word=text.split()
count=0
broken=set(brokenLetters)
for char in word:
            if char not in broken :
                count+=1
print(count)