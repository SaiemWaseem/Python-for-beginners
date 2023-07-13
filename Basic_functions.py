num = [1,2,2,4,5,6]
print(4 in num)
(num.sort())
num.reverse()
print(num)
# write a program to make duplicate of the list
num = [2,2,3,3,1,6,7,5,6]
uniques = []
for nums in num:
    if nums not in uniques:
        uniques.append(nums)
print(uniques)
# tuples
num =(1,2,3)
print(num[0])
num= (2,3,4)
x,y,z= num
print(x)
customer = {
    "name":"Sam",
    "age" : 19,
    "is_verified": True
}
print(customer["age"])
print(customer.get("birthdate","Sep 15 2003"))
customer["name"]="Sami"
print(customer)
phone = input("Phone: ")
digit = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output= ""
for ch in phone:
    output += digit.get(ch,"!")+" "
print(output)
message = input(">")
words = message.split(' ')
emojis = {
    ":)":"😊",
    ":(":"😢"
}
output=""
for word in words:
    output+= emojis.get(word,word)+" "
print(output)
try:
    age=int(input('age: '))
    risk = 20000
    income = risk/age
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("Invalid Error")
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


Point1=Point()
Point1.x= 10
Point1.y = 20
print(Point1.x)
Point1.draw()


