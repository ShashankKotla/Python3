#Numbers : Int, Float, complex
#Int => +ve or -ve, without decimals of unlimited length.
# x = 1
# y = 238940583045
# z = -44934
# print(type(x))
# print(type(y))
# print(type(z))

#Float -> +ve or -ve with decimals
# x = 1.0
# y = 23.8940583045
# z = -44.934
# print(type(x))
# print(type(y))
# print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# x = 23e3
# y = 12E4
# z = -89.7e100
# print(type(x))
# print(type(y))
# print(type(z))


#complex -> written a 'j' as the imaginary part.

# x = 3+5j
# y=5j
# z=-5j

# print(type(x))
# print(type(y))
# print(type(z))

# Type-conversion
# x = 1
# y = 2.8
# z = 1j

# a = float(x)
# b=int(y)
# c = complex(x)

# print(a)
# print(b)
# print(c)


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 10))
# Display's num from 1to9

