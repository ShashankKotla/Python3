# Python3-Created by Gudio Van Rossum & released in 1991
# it is platform independent & used for Web Dev, software Dev, mathematics, system scripting.
# Python uses indentation to indicate a block of code. & no.of spaces should be 4 or 2 or atleast 1

# Comment:- #, single line comment & """ """, Multiline comment.

#variables:- It is a container to store data values & they are case-sensitive. 
# x = 5
# y = "john"
# print(x)
# print(y)

# Casting :- int(), str(), float()

# x = str(3)
# y = int(3)
# z = float(3)
# print(x)
# print(y)
# print(z)


# multiple variables

# x, y, z = "orange", "Banana", "cherry" #Multi-value to Multi-variable
# x = y = z = "orange" #one value to multi-variables.

# print(x)
# print(y)
# print(z)

#Unpacking a collections
#  extract the values into variables from collection of values in a list , tuple etc.
val = [9, 8, 7, 6]
# x, y, z, v = val
# print(x)
# print(y)
# print(z)
# print(v)

# print(x, y, z, v)
# print(x+ y+ z+ v)


# x = 'first'
# def myfun():
#     x = "second"
#     print(x)
# myfun()

# print(x)

# def test():
#     global x
#     x = "fantastic"
# test()
# print("here:", x)

# for i in "hi":
#     global x
#     x = 'hlo'
#     print(i)
# print(x)

# x = "hi1"
# def myfun():
#     global x
#     x = "hi-2"
# myfun()
# print(x)