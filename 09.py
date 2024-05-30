# Write a Python Program to call data members and functions using classes and objects.

class Car :
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def car_name(self):
        return(f"{self.brand} {self.model}")

my_car = Car("TATA","Safari")

print(f'Car Brand: {my_car.brand}')
print(f'Car Model: {my_car.model}')

print(my_car.car_name())