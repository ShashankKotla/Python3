#A Class is like an object constructor, or a "blueprint" for creating objects.

# class My_class:
#     x = 5


# p1 = My_class()
# print(p1.x)


#Note : All classes have a function called __init__(), which is always executed when the class is being initiated.
#__init__() function is called automatically every time the class is being used to create a new object.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("John", 36)
# print(p1.name)



#class with __str__() function.
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self) -> str:
#         return f'{self.name} ({self.age})'
# p1 = person('JOHN', 36)
# print(p1)


# __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned: <__main__.Person object at 0x15039e602100>

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def myfun(self):
#         print("Hello, my name is " + self.name)
# p1 = Person("John", 36)
# p1.myfun()
#Note : Objects can also contain methods. Methods in objects are functions that belong to the class.



#self parameter - It is a reference to the current instance of the class, and is used to access variables that belongs to the class

# class Details:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def my_fun(self):
#         print(self.name)
    
# p1 = Details('marko', 47)
# p1.my_fun()


# class details:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return f'{self.name}'
# d = details('shashank')
# print(d)
# print(d.__str__())


# class Person:
#     def __init__(timeWasteFellow, name, age) -> None:
#         timeWasteFellow.name = name
#         timeWasteFellow.age = age
    
#     def myfun(wasteFellow):
#         print(f'Name of timeWasteFellow: {wasteFellow.name} & his age is: {wasteFellow.age}')


# waste = Person('Shashank', 22)
# waste.myfun()

# waste.name = 'Thor'
# waste.myfun()

# del waste.age
# waste.myfun()

#Pass Statement

# class Person:
#     pass