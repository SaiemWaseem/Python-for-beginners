# higher order function
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide = divisor(2)
print(divide(10))

# lamda parameter:expression

double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z:x+y+z
print(multiply(2,5))
print(double(5))
print(add(2,5,6))
age_check = lambda age:True if age >= 18 else False
print(age_check(19))

# sort() method = used with lists
# sort() function = used with iterables

Jigriyawr = ["Jessica","Bareera","Shelli","Saneha"]

Jigriyawr.sort(reverse=True)

for i in Jigriyawr:
    print(i)

Jigriyawr = ("Jessica","Bareera","Shelli","Saneha")

# Jigriyawr.sort(reverse=True)
sorted_J = sorted(Jigriyawr)

for i in sorted_J:
    print(i)

# sort() function
students = [("Saim","A",77),
            ("Sam","B+",70),
            ("Sami","A+",85),]

grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)
sorted_students = sorted(students,key=grade)

for i in students:
    print(i)

# warlus operator
foods = list()
while food := input("what food do you like? ") != "quit":
    foods.append(food)
# map() function only applicable to iterabels (list or tuple)
store = [("shirt",25),
         ("pent",10),
         ("shoes",50)]
to_dollar = lambda data: (data[0],data[1]*285)
store_dollar = list(map(to_dollar,store))

for i in store_dollar:
    print(i)
# filter() function
students = [("Saim",17),
            ("Sam",20),
            ("Sami",18),
            ("Musa",15)]
age = lambda data: data[1] >=18
import functools
letter = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letter)
print(word)
factorial= [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorial)
print(result)
# list comprehesion use less syntax     list =[expression for item in iterable]
#                                       list =[expression for item in iterable if conditional ]
#                                       list =[expression if/else for item in iterable]
square = []
for i in range(1,11):
    square.append(i*i)
print(square)
square = [i*i for i in range(1,11)]
print(square)
student = [20,40,50,100,60,90]
passed_student = [i if i>=60 else "hard" for i in student ]
print(passed_student)
