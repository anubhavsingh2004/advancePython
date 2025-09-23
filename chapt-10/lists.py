# lists in python:
# list is a collection of items- that are ordered, changable, from diff datatypes (duplicates are allowed)

colors=["red","blue","green","yellow"]
print(colors)

#Accessing a list element: 
# done by index
nums=[2,5,8,6,78]
print(nums[2])
print(nums[-3])

# list slicing :
# list[start, stop, step]
# start elem in list is inclusive
# stop elem in lists is exclusive
num3=[5,4,6,8,5,7,56]
print(num3[1:3])
print(num3[2:6])       

# List methods:
# appdemd():
nums_1=[1,2,3,5,6,9]
nums_1.append(5)
print(nums_1)

#2 extend():
nums_1=[1,2,3,5,6,9]
nums_2=[25,45,18,70]
nums_1.extend(nums_2)
print(nums_1)

# insert():
nums_1=[1,2,3,5,6,9]
print(nums_1)
nums_1.insert(3,100)
print(nums_1)

# remove():
colors=["r","b","g"]
print(colors)
colors.remove("b")
print(colors)

# count():
print(colors.count("b"))

# pop():
colors=["r","b","g"]
print(colors)
colors.pop()
print(colors)
colors.insert(2,23)
colors.insert(3,"b")
colors.pop(3)
print(colors)

# clear():
# colors.clear()
# print(colors)

# index():
print(colors.index("b"))

# sort():
nums_1.sort() #by default gives ascend order
print(nums_1)
nums_1.sort(reverse=True) #gives sort in descend order
print(nums_1)


#joining two lists:
list1=[1,2,3]
list2=["a","b",2]
#method 1 : using the + operator:
list3= list1+list2
print(list3)
# method 2: using the append method:
list4=[56,4]
list5=[5,98,74]
for x in list5:
    list4.append(x)
print(list4)
#method 3 : using the extend methods:
list45=[56,4]
list55=[5,98,74]
list45.extend(list55)
print(list45)