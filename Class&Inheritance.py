# Inheritance
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("talk")


jhon = Person("Sam")
print(jhon.name)
jhon.talk()
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class cat(Mammal):
    def meow(self):
        print("mewo")


cat1 = cat()
cat1.meow()
dog = Dog()
dog.walk()

# Weight Converter
import converter
print(converter.lbs_to_kg(150))




