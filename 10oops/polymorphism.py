# 'polymorphism' means 'many forms'
#In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.



#function polymorphism -> example: len()

#1.str
x = 'python function'
# print(len(x))

# 2. list
y = ['python', 'function']
# print(len(y))

#3.tuple
z = ('python', 'function')
# print(len(z))


#class polymorphism -> it can often used in cls methods, where multiple class have same method.


# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     x.move()


#Inheritance class polymorphism:

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Move!")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self):
#         print("Fly")
    
# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()





# class One:
#     def __init__(self) -> None:
#         pass
#     def val(self):
#         print("This is one!")

# class Two(One):
#     def __init__(self) -> None:
#         pass
#     def val(self):
#         # print("This is two!")
#         pass

# o = One()
# t = Two()

# for x in (o, t):
#     print(x.val())