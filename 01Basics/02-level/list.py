#Ordered, changable, allow duplicates
#list items accessed by indexed-[]

# l = ["one", 1, 3.0, True] #contains different DT
# print(l)
# l1 = list(("one", 1, 3.0))
# print(l1)


# l2 = ["one", 2, 3.3]
# print(len(l2))
# print(type(l2))

#Access items
# print(l2[2])
# print(l2[-1])

# if "one" in l2:
#     print("It is present")
# else:
#     print("It is not present")


#Change items

items = ["One", "elephant", 3, 5.4, "Mercury", "mars"]
# items[0] = "Two"
# items[1:4] = ["Elephant", 49, 5.6] # change range of items
# items.insert(2, 54) #without replacing any of the existing values
# items.append("rat")
# items2 = ["rat", "camel"]
# items.extend(items2)
# items.remove("mars")
# print(items)
# items.pop(4) #remove specified index.
# del items
# items.clear()
# print(items)

# for x in items:
#     print(x, end=',')

# for x in range(len(items)):
#     print(items[x])


# i=0
# while i<len(items):
#     print(items[i])
#     i=i+1


#List Comprehension
num = ["one", "two", "three","four", "five"]
# num1 = []
# for x in num:
#     if 'f' in x:
#         num1.append(x)
# print(num1)

# num1 = [x for x in num if 'f' in x]
# print(num1)

# num1 = [x for x in range(5)]
# num1 = [x.upper() for x in num]
# print(num1)
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list


# n2 = ["hello" for x in num]

# print(n2)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# n1 = [x if x!='banana' else 'orange' for x in fruits]
# print(n1)

# fruits.sort()
# fruits.sort(reverse=True)
# print(fruits)


#customize sort function

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc) 
print(thislist)


#note: Here's a breakdown using your example:
# myfunc(100) returns abs(100 - 50), which is 50.
# myfunc(50) returns abs(50 - 50), which is 0.
# myfunc(65) returns abs(65 - 50), which is 15.
# myfunc(82) returns abs(82 - 50), which is 32.
# myfunc(23) returns abs(23 - 50), which is 27.
# Now, the list is sorted based on these calculated values:

# 0 (for 50)
# 15 (for 65)
# 27 (for 23)
# 32 (for 82)
# 50 (for 100)
# So, after sorting, the list becomes [50, 65, 23, 82, 100]. The sort method uses these calculated values as keys to determine the order of elements in the sorted list. The original values in the list remain unchanged.


#Case Insensitive Sort
# n = ["one", "Two", "three", "Four", "Five"] 
# n.sort() #case sensitive
# n.sort(key = str.lower) #case In-sensitive
# print(n)

#reverse
# n.reverse()
# print(n)

#Copy A List
# n = ["one", "Two", "three", "Four", "Five"] 
# n2 = n.copy()
# print(n2)
# n3 = list(n)
# print(n)


# n3 = ['six', 'seven']
# print(n+n3)
# n3.append(n)
# print(n3)

# import tuple
# print(tuple.addon(2,4))