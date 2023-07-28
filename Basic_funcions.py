name = ""
import time
while len(name) == 0:
    name = input("enter your name; ")
print("Hello "+name)
for i in range(10):
    print(i+1)
for i in range(50,100+1,2):
    print(i)

for i in "Sam Code":
    print(i)
for second in range(10,0,-1):
    print(second)
    time.sleep(1)
print("Happy New Year!")
row = int(input("how man rows?"))
columns = int(input("How many columns?"))
symbol = input("Enter a symbol to use: ")
for i in range(row):
    for j in range(columns):
        print(symbol,end="")
    print()
while True:
    name = input("enter your name: ")
    if name != " ":
        break
phone_number = "305-5803589"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")
for i in range(1,21):

    if i ==13:
        pass
    else:
        print(i)
food = ["pizza","burger","shwarma","pepsi"]
food[3]= "sushi"
print(food)
food.append("fries")
print(food)
food.remove("pizza")
print(food)
# 2D list
drinK = ["coeffe","pepsi","soda","tea"]
dinner = ["rice","biryani","corma"]
desserts = ["faludha","cake","rabri dhood"]

food = [drinK,dinner,desserts]
print(food[0][3])
# tuple
student = "Sam Bro"
print(student.count("Sam"))
for i in student:
    if i == "Sam Bro":
        break
print(i)
# sets
dishes = {"plates","bowl","knife"}
utensiles = {"fork","spoon","knife"}
utensiles.add("napkin")
print(utensiles)
dinner_table = utensiles.union(dishes)
print(dinner_table)
utensiles.difference(dinner_table)
print(utensiles)
common = utensiles.intersection(dishes)
print(common)
# Dictionary
capitals = {'Usa':'Washington DC',
            'india':'New dehli',
            'Russia':'Moscow'}
capitals.update({'Germany':'Berlin'})
capitals.update({'Usa':'Las vegas'})
print(capitals.pop('india'))
print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
# indexing
name = "sam Bro"
if(name[0].islower()):
    name = name.capitalize()
first_name = name[0:3].upper()

print(first_name)
# Function
def repeat():
    print("i will not repeat my code")
repeat()
name = 'Sam'
def hello(name):
    print('hello '+name)
    print("have a nice day!")
hello("Sam")
def hello(first_name,last_name,age):
    print("hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")
hello("Bro","Sam",19)
# return statement:
def multiply(num1,num2):
    result = num1*num2
    return result
print(multiply(3,2))
# keyword arguments
def hello(first_name,middle,last_name,):
    print("hello "+first_name+" "+middle+" "+last_name)

hello(first_name="Sam",middle="Bro",last_name="Awesome")
# nested functions
name = round(abs(float(input("Enter a positive number : "))))
print(name)
# scope
name = "Sam"
def display_name():
    name = "code"
    print(name)
display_name()
print(name)
"*args"
def add(*args):
    sum = 0
    args = list(args)
    args[0]= 0
    for i in args:
        sum += i
    return  sum


print(add(1,2,3,4,5,6,7))
# **kwargs : parameters that will pack all arguments in dictionary useful so that a function can accept a varying amount of arguments.
def hello (**kwargs):
    print("Hello " +kwargs['first'] + " " + kwargs['last'])
    print("hello")
    for key,value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.",first="sam",middle="dude",last="Bro")
str.format
animal = "Cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
print("The {animal} jumped over the {item}".format(animal='Cow',item='moon'))
text = "the {} Jumped over the {}"
print(text.format(animal,item))
name = "Bro"
print("My name is {}".format(name))
name = "Bro"
print("the {} left school".format(name))
print("my name is {:10}. Nice to meet you".format(name))
number = 1000
print("the number pi is {:.2f}".format(number))
print("the number pi is {:.3f}".format(number))
print("the number is {:,}".format(number))
print("the number  is {:b}".format(number))
print("the number  is {:o}".format(number))
print("the number  is {:x}".format(number))
print("the number  is {:E}".format(number))
import random
X = random.randint(1,6)
y = random.random()
my_list = ["rock","paper","scissor"]
z = random.choice(my_list)
print(z)
cards = [1,2,3,4,5,6,7,8,'j','q','K']
random.shuffle(cards)
print(cards)


# MODULES IN PYTHON :- Make a modlue of messages and def their hello or bye function and then you will learn how module work in python and takes value from the module.
import messages as msg
from messages import hello,bye
hello()
bye()
messages.hello()
messages.bye()
msg.hello()
msg.bye()



