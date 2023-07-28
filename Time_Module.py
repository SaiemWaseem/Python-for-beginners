# Time Module
import datetime
now = datetime.datetime.now()
print("current date and time")
print(now)
# dictionary comprehension
# dictionary = {key: expression for (key,value) in iterables}
#  dictionary = {key: expression for (key,value) in iterables if condition}
#  dictionary = {key: (if/else) for (key,value) in iterables if condition}
#  dictionary = {key: function_value for (key,value) in iterables if condition}
import time



cities_F = {'lahore':90,'karachi':150,'peshawar': 130}
cities_C = {key: round((value-32)*(5/9)) for (key,value) in cities_F.items()}
cities_C = {key: round((value-32)*(5/9)) for (key,value) in cities_F.items() if value == 130}
cities_C = {key: ("Warm" if value >= 100 else "Moderate") for (key,value) in cities_F.items()}
print(cities_C)
# zip(* iterables)

username = ["bro","Sam","code"]
passwords = ("p@ssword","abc123","guest")

users =dict(zip(username,passwords))

print(type(users))

for key,value in users.items():
    print(key+" : "+value)
import time
print(time.ctime(1000000))

print(time.time())

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_string = '''20 April, 2023'''
time_object = time.strptime(time_string,'''%d %B, %Y''')
print(time_object)

time_tuple = (2023, 6, 7, 4, 31, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
# time_string = time.mktime(time_tuple) #for second
print(time_string)

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drink coffee")

def study():
    time.sleep(5)
    print("You finish study ")

x = threading.Thread(target =eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

#
eat_breakfast()
drink_coffee()
study()

print(threading.active_count())
print(threading.enumerate())    # enumerate function is used to print the list while running the thread
print(time.perf_counter())
import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()


answer = input("Do you wish to exit?")
#__________________________
 # Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(100000000,))
    # b = Process(target=counter, args=(500000000,))

    a.start()
    # b.start()

    print("processing...")

    a.join()
    # b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()
