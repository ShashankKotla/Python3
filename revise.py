# Write a Python program to count the number of vowels in a given string.
# x = "a,e,i,o,u"

# nums = [1, 2, 3, 4]
# squares = [x**2 for x in nums if x % 2 == 0]
# print(squares)



# File Handling: Write code to:

# Open a file named data.txt in append mode

# Write "Hello, World\n" to it

# Then read and print its content


# with open("data.txt", "x") as dt:
#     dt.write("Hello, World \n")
#     dt.close()

# with open("data.txt", "r") as dt:
#     print(dt.read())
#     dt.close()

# Write a function that takes a list of numbers and returns only the even ones.

x = [1,2,3,4,5,6]

# for i in x:
#     if i % 2 == 0:
#         print(i)

# def even(x):
#     for i in x:
#         if i % 2 ==0:
#             print(i)

# print(even(x))

# my_list = [0, '', [], {}, None, 'Python']
# print([bool(x) for x in my_list])

# OOP: Define a Person class with:
# name, age attributes
# a method greet() that returns "Hello, I am {name}"



# class Person:
#     name = 'Shashank'
#     age = 24

#     def greet(self,name, age):
#         self.name = name
#         self.age = age
#         print(f"Hi There! {self.name}. Happy {self.age}th bday!")

    
# Person.greet()

# name = 'shashank'
# age = 24

# def greet():
#     print(f"Hi There! {name}. Happy {age}th bday!")

# greet()

# class Person:
#     name = 'shashank'
#     age = 24

#     def greet():
#         print(f"Hi There! {name}. Happy {age}th bday!")

# x = Person.greet()
# print(x)

# def foo(x, y, /, z):
#     print(x, y, z)

# foo(1, 2, z=3)

di = {
    'one':1,
    'two' : 2
}

