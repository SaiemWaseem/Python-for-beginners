
# Import from the module Car
from car import Car

car_1 = Car("Germany","Audi","23","blue")
car_2 = Car("Germany","Mercedes","23","blue")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print(car_1.wheels)

car_1.drive()
car_1.stop()

