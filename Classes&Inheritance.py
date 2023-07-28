# Example Number 1 Classes
# A class is a blueprint for creating objects with specific attributes and methods. It is a fundamental concept in object-oriented programming (OOP) and allows you to create custom data types to model real-world entities or abstract concepts

from abc import ABC,abstractmethod

class Vehical(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehical):
    def go(self):
        print("You drive the car! ")
    def stop(self):
        print("You stop the car! ")
class Motorcycle(Vehical):
    def go(self):
        print("You drive the motorcycle! ")
    def stop(self):
        print("You stop the motorcycle! ")

car = Car()
Motorcycle = Motorcycle()

car.stop()
Motorcycle.go()
Motorcycle.stop()
#
# Example Number 2  Object as Arguments
class Car():

    color = None
def color_change(car,color):
    car.color = color
class Motorcycle():

    color = None
def color_change(Motocycle,color):
    Motocycle.color = color

car_1 = Car()
color_change(car_1,"Black")
print(car_1.color)
say = print
say("Sam bro ")

# Example Number 3
class FastFood:

    def eat(self):
        print("he can eat Pizza")

class drink:
    def drink(self):
        print("he will drink coke!")
class Ali(FastFood):
    pass
class Musa(drink):
    pass
class Sam(FastFood,drink):
    pass

Ali = Ali()
Musa = Musa()
sam = Sam()
Ali.eat()
Musa.drink()
sam.drink()
# Example number 4
class Car:

    def turn_on(self):
        print("your car is turn on")
        return self
    def drive(self):
        print("you drive the car ")
        return self
    def brake(self):
        print("you step on the brake ")
        return self
    def stop(self):
        print("you stop the car ")
        return self

car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .stop()

# Example Number 5 Inheritance:
# Inheritance is an essential concept in object-oriented programming (OOP) and is supported by Python. It allows you to create a new class that inherits the properties and behaviors (attributes and methods) of an existing class, known as the base class or parent class. The new class is called the derived class or subclass. Inheritance promotes code reuse and enables you to create more specialized classes based on existing ones.

class Waseem:
    Human = True
    def Honest(self):
        print("very honest in fairs")
    def generous(self):
        print("very generous to others!")

class Saiem(Waseem):
    def study(self):
        print("I'm studying day and night and become python developer and data scientist ✔✨ ")
class Jessica(Waseem):
    def Art(self):
        print("I can take admission in the Architect 😉")
class Mehak(Waseem):
    def Engineer(self):
        print("I complete my degree nearer😁")
class Saneha(Waseem):
    def computer(self):
        print("I will become computer engineer in future 🤞")

Saiem = Saiem()
Saneha = Saneha()
Jessica = Jessica()
Mehak = Mehak()

print(Saiem.Human)
Mehak.Engineer()
Saneha.computer()
Jessica.Art()
#
# # multi-level-inheritance:
# Multilevel inheritance is a type of inheritance in object-oriented programming where a class derives from another class, which itself is derived from yet another class. This creates a chain of inheritance, where each class acts as both a subclass (derived class) and a base class (parent class) simultaneously.
class Organism:

     alive = True

class Animals(Organism):
     def eat(self):
         print("This animals is eating")

class Dog(Animals):
    def bark(self):
        print("This dog is barking ")
# overriding
class Dog(Animals):
    def bark(self):
        print("the dog is yelling")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

