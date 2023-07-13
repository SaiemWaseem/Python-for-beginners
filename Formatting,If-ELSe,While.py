import math
# formatting in strings
first = "Sam"
last = "Waseem"
message = first + '[' +last + '] is a coder'
msg = f'{first} [{last}] i a coder'
print(msg)
course = 'python for Sam'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('SM'))
print(course.replace('Sam','Saiem'))
print('Sam'in course)
print(5**2)
x = 5
y = 5+x
print(y)
x -= 2
print(x)
x = (2+3)* 10 - 3
print(x)
x=3.9
print(round(x))
print(abs(-x))
import math
print(math.floor(2.9))

# If-Else condition
is_hot = False
is_cold = False

if is_hot:
    print("it's a hot day")
    print ("drink plenty of water ")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day ")
print ("enjoy your day ")
price = 1000000
good_credit = True
if good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print (f"Down payment: ${down_payment}")
criminal_record = False
good_credit = True

if good_credit and not criminal_record:
    print("eligible for loan ")
else:
    print ("Not Eligible")
temperature = 31
if temperature!=31:
    print("it's a hot day ")
else:
    print("pleasant day ")
name = "Saiem"
if len(name) < 3 :
    print ("must al least 3 character ")
elif len(name) > 50:
    print(" name must b maximum 50  ")
else:
    print(" name looks good!")
weight = int(input("weight: "))
unit = input("(L)lbs or (kg)kilos: ")
if unit.upper() == "L":
    converted = weight*0.45
    print(f"your weight is{converted}kilos ")
else:
    converted = weight/0.45
    print(f"your weight is{converted}pounds")

# While loop
i =1
while i<=5:
    print ("*" *i)
    i=i+1
print("done")
secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_num:
        print("you won!")
        break
else:
    print("Sorry! Friend you are Failed.. ")








