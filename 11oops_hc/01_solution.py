class Car:
    total_car = 0
    
    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + '!'

    def full_name(self):
        return f"FullName: {self.brand + ' ' +self.__model}"
    
    def fuel_type(self):
        return "Petrol car"
    
    @staticmethod
    def general_description():
        return "Car used my human beings to travel"
    
    @property #Hides the property allow to read only.
    def model(self):
        return self.__model

# my_car = Car("Toyota", "Carola")
# print(my_car.brand)
# print(my_car.full_name())

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size) -> None:
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"





# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# print(Car.total_car)

# my_car = Car("Tata", "safari")
# print(my_car.general_description())
# print(Car.general_description())
# print(my_car.model)


class Battery:
    def battery_info(self):
        return "Battery"


class Engine:
    def engine_info(self):
        return "Engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("tesla", "modelS")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
