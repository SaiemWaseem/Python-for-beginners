# No.1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are ")
# No.2
import sys

print("Python Version")
print(sys.version)
print("Version info")
print(sys.version_info)
# No.3
import datetime
import time

now = datetime.datetime.now()
print("Current Date and time:")
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# No.4
from math import pi
r = float(input("Enter the radius of circle: "))
print("The area of the circle with radius  " + str(r) + "is:"+str(pi*r**2))
# No.5
first = input("Enter your Name: ")
last = input("Enter last Name: ")
print(last+" "+first)
# No.6
numbers = input("Enter some numbers separated with commas: ")
list = numbers.split(",")
tuple = tuple(list)
print("list : ", list)
print("tuple :", tuple)
# No.7
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
# No.8
color_list = ["Red","Green","White","Black"]
print(color_list[0],color_list[3])
# No.9
exam_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_date)
# No.10
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print(n1+n2+n3)
# No.11
print(abs.__doc__)
# No.12
import calendar
y = int(input("Input the Year : "))
m = int(input("Input the month : "))
print(calendar.month(y,m))
# No.13
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
# No. 14
from datetime import date
date1 = date(2014,7,2)
date2 = date(2014,7,11)
days = date2 -date1
print(days.days)
# No. 15
from math import pi
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',round(V))
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(22))
print(difference(14))
# No.17
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
# No.18
def sum_thrice(x, y, z):

     sum = x + y + z

     if x == y == z:
      sum = sum * 3
     return sum

def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text
print(sum_thrice(3, 2, 3))
print(sum_thrice(3, 3, 3))

# No.19
def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text
  return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty"))
# No.20
def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result
print(larger_string('abc', 2))
print(larger_string('.py', 3))
# No. 21
def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 5:
      count = count + 1

  return count

print(list_count_4([5, 4, 5, 5, 4]))
print(list_count_4([1, 4, 5, 5, 7, 4]))
# 21
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
# No.22
def substring_copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
    substr = text[:flen]
    result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))
# No. 23
def is_vowel(alph):
    al_v = "aeiou"
    return alph in al_v
print(is_vowel('a'))
print(is_vowel('b'))
# No.24
def value_G(data, n):
    for value in data:
        if n == value:
            return True
    return False
print(value_G([1, 5, 8, 3], 3))
print(value_G([5, 8, 3], -1))
# No.25
def histogram(items):
    for n in items:
        output = ''
        times = n
        while(times > 0):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])
# No.27
def concatenate_list_data(list):
    result = ""
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))
# No.28
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
# No.29
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
# No. 30
b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)
# No. 31
def gcd(x, y):
   gcd = 1
   if x % y == 0:
       return y
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
   return gcd
print("GCD of 12 & 17 =",gcd(12, 20))
print("GCD of 4 & 6 =",gcd(4, 16))
print("GCD of 336 & 360 =",gcd(300, 360))
# No. 32
def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(4, 6))
print(lcm(15, 17))
# No. 33
def sum_3(x, y, z):
    if x==y and y==z and z==x:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_3(2,3,5))
print(sum_3(1,1,1))
# No. 34
def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 5))
# No. 35
def test_number5(x, y):
   if x == y or abs(x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
# No. 36
def num(a,b):
    if not (isinstance(a, int)) and (isinstance(b, int)):
        return "invalid "
    return a+b
print(num(2,6))
print(num(1,7))
# No. 37
print("Name: Sam\nAge: 19 \nAddress: H No.127")
def personal():
    Name, age = "Sam",19
    Address = "Uet Lahore.."
    print("Name: {}\nAge: {}\nAddress: {}".format(Name,age,Address))


personal()
# No. 38
x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))
# No. 39
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,3))
# No. 40
import numpy as np
p1 = [4, 0]
p2 = [6, 6]
dis = np.sqrt(((p1[0]-p2[1])**2)+((p1[1]-p2[0])**2))

print(round(dis))
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, "k" , marker = 'p', ms = 20)
plt.show()
import os.path

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5', c = "k",ls = ":", marker = "p" )
plt.show()
# No. 41
import os.path
print(os.path.isfile("Practice_MixFunc.py"))
print(os.path.exists("Practice_MixFunc.py"))
file = open("W3resources Practice❤🤍.txt")
try:
    file = open("W3resources Practice❤🤍.txt")
    file.close()
    print("file found")
except FileNotFoundError:
    print("File not found!")
# No. 42
import platform, struct
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)
import struct
print(struct.calcsize("P")*8)
# No. 43
import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())
# Method II
import os
import sys
import platform
import sysconfig
print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())
# No.44
import site;
print(site.getsitepackages())
# No. 45
import os
print("Current File Name : ",os.path.realpath(__file__))
# No. 46
def test(s):
   try:
       return int(s)
   except ValueError:
       return float(s)
print(test('12'))
print(test('200.999'))
# No.47
for i in range(0, 10, 2):
    print('*', end="")
print("\n")
# Method II
import functools
printf = functools.partial(print, end="")
for i in range(0, 10):
   printf('*')
   i = 0
# No. 48
import cProfile
def sum():
    print(3**3)
cProfile.run('sum()')
# No. 49
import getpass
print(getpass.getuser())
# No.50
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
# No. 51
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)
# No. 52
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)
# No. 53
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c)
# No. 54
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)
# No. 55
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("Practice_MixFunc.py")))
print("Created: %s" % time.ctime(os.path.getctime("Practice_MixFunc.py")))
# No. 56
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
# No. 57
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
s = "The quick brown fox jumps over the lazy dog."
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))
print(copyright())
# No. 58
import os
file_size = os.path.getsize("Practice_MixFunc.py")
print("\nThe size of file is :",file_size,"Bytes")
print()
# No. 59
n=1
if n == 1:
   print("\nFirst day of a Month!")
# No. 60
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
# No. 61
num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)
# No. 62
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
# No. 63
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums)
# No. 64
from functools import reduce
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = reduce( (lambda x, y: x * y), nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)
# No. 65
print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
# No. 66
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())
# No. 67
x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")
# No. 68
import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))
# No. 69
import json
x = json.dumps({'sam':1, })
print(x)
# No. 70 (HOME DIRECTORY)
import os.path
print(os.path.expanduser('~'))
# No. 71
print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)
# No.72
def sum_of_cubes(n):
 n -= 1
 total = 0
 while n > 0:
   total += n * n * n
   n -= 1
 return total
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))
# no. 73
def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
  return False
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));
print(dt3, odd_product(dt3));
# conditional and loops
# No.1
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
# No.2
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
# No.3
import random
guess = 0
target_no = random.randint(1, 10)
while target_no != guess:
    guess = int(input("Guess a number: "))
print("Well Guessed! ")
# No.4
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
# No.5
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")
# No.6
numbers = (1, 2, 6, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
# No.7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
# No.8
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print('\n')
# No.9 (Fibonacci series)
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y
# No.10
for fizzbuzz in range(21):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
# No.11
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
# No.12
items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))

