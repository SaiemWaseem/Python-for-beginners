class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1= Point(10,20)
Point1.x= 10
print(Point1.x)

#_______________________________________

def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print("welcome abroad!")


print("start")
greet_user("Sam","Waseem")
print("finsih")
def square(number):
    return(number*number)
print(square(3))
try:
    age= int(input('Age: '))
    print(age)
except ValueError:
    print("invalid Syntax")
class Point:
    def move (self):
        print('move')
    def draw (self):
        print("draw")


point1 = Point()
point1.x= 10
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

