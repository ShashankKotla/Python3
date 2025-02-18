# Abstraction, Simplifies complex systems by focusing on essential characteristics while hiding unnecessary details.
# It can be achieved through abstract base class (ABCs), abstract methods, and interfaces

# Link :- https://medium.com/pythons-gurus/3-simplifying-complexity-with-abstraction-in-python-7aa8f76c45af#:~:text=Abstraction%20is%20a%20fundamental%20concept,%2C%20abstract%20methods%2C%20and%20interfaces.

from abc import ABC, abstractmethod

class Vechile(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    
    @abstractmethod
    def drive(self):
        pass 

#Concrete Subclasses 
class Car(Vechile):
    def drive(self):
        return f"{self.brand} {self.model} is driving on the road."
    
class Boat(Vechile):
    def drive(self):
        return f"{self.brand} {self.model} is sailing on the water."

car = Car("Toyota", "corolla")
boat = Boat("Yamaha", "275SD")

print(car.drive())
print(boat.drive())
