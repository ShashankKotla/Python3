#Ordered & unchangable, allows duplicates

tu = ("One", 3.5, 33, 33)
# print(type(tu))
# print(tu)
# print(len(tu))

# tu2 = ("apple",)
# print(tu2)
# print(type(tu2))

# print(tu.count(33))
# print(type(tu))

# tu2 = tuple(('two', 22, 4.6))
# print(tu2)


t = ("One", 2, 2.2, "three", "Four")
# print(t[-1])
# print(t[-4:-1])

#check if item exist
# if "Four" in t:
#     print('present')
# else:
#     print("Not Present")

#change
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = 'orange'
# y.append('orange')
# y.remove('banana')
# x = tuple(y)
# y = ('orange',)
# x += y
# print(x)


#packing & unpacking

# A tuple normally assigned with values called packing.
# Extract values back into variables, called unpacking.

# x = ("apple", "banana", "cherry") #Packing

# (green, red, blue) = x #unpacking

# print(green)
# print(red)
# print(blue)


#Asterisk * -> "assigning it to a variable, gives power to take more than one value."

# color = ('white', 'red', 'green', 'yellow', 'blue', 'brown')

# (one, two, *three) = color
# (one, *two, three) = color
# print(one)
# print(two)
# print(three)


#loop
color = ('white', 'red', 'green', 'yellow', 'blue', 'brown')
# for c in range(len(color)):
#     print(color[c])

# def addon(num1, num2):
#     return num1 + num2


# i = 0
# while i < len(color):
#     print(color[i])
#     i = i + 1

# color2 = ("maroon", "purple", "black")
# color3 = color + color2
# print(color3)

# color4 = color * 2
# print(color4)