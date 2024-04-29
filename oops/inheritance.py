#Inheritance :- Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#Parent Class
# class Person:
#     def __init__(self, fname, lname) -> None:
#         self.fname = fname
#         self.lname = lname

#     def print_name(self):
#         print(f'Full Name: {self.fname} {self.lname}')

# name = Person('Shashank', 'Kotla')
# name.print_name()

#Child Class
# class Student(Person):
    # def __init__(self, fname, lname):
    #     Person.__init__(self, fname, lname)
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

    # def __init__(self, fname, lname, graduation_year) -> None:
    #     super().__init__(fname, lname) # super() function that will make the child class inherit all the methods and properties from its parent
    #     self.graduation_year = 2023
    #     self.graduation = graduation_year

#     def welcome(self):
#         print(f'Hi There! I\'m {self.lname} {self.fname} and i\'m a CSE graduate-{self.graduation} passout student.')


# name2 = Student('kotla', 'shashank', 2023)
# # name2.print_name()
# print(name2.graduation)
# name2.welcome()

#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.




class Details:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def out(self):
        print(self.name , self.age)

# obj1 = Details('shashank', 22)
# print(obj1.out())

class Full(Details):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def det(self):
        print(f'{self.name}, {self.age}, {self.country}')

# obj1 = Details('shashank', 25)
# print(obj1.out())

obj = Full('test', 20, 'Unknown')
obj.out()
