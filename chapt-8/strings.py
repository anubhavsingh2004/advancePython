name="anubhav is a boy"
print(type(name))

#formatting in python strings
#str.format() method
name="madhav"
age=30
print("my name is {} and im {}".format(name, age))

#f strings
name="madhav"
age=30
print(f"my name is {name} and im {age}")
print(f"in 5 yrs time ill be {age+5}")# in f strings we can perform oprations

#escape characters:
print ("hello\nim anubhav")# \n is for line break
print ("hello\tim anubhav")# \t is for tab spacing

strings_ex="im anubhav and i love coding in python"
print("hello " +strings_ex)
name="anubhav"
print(name*3)
p=name[3]
print(p)
s=name[3:-1]
print(s)
ss=name[1:15:2]# no errors jitna hai utna print hoga
print(ss)
print(len(ss))
print(name[::-1])
print(name[-1::-1])
print(name[-1:])

#STRING MTHODS:
#len(), upper(), count(), find(), split(),replace(), tilte(),strip(),
print("string methods\n")
word="ankurrwa"
print(f"num of chars in word are {len(word)}")
print(f"word in uppercase is {word.upper()}")
print(f"the char a is at {word.find("a")}")
print(f"num of r in word are {word.count("r")}")
print(f"replace the word ankurrwa with ankurwa :{word.replace("ankurrwa", "ankurwa")}")

word_extnded="ankur is a banana"
print(f"using split method: {word_extnded.split("-")}")#will check if there is a - and will split based on -
print(f"using split method: {word_extnded.split()}")#will split on whitspaces
print(f"using title method  : {word_extnded.title()}")#to make each part of string a capital
