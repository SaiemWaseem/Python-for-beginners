for name in 'jessica':
    print(name)
for item in range (5,10,2):
    print (item)
for name in ['Sam','sami','Saiem']:
    print(name)
for x in [1,2,3,4,5]:
    print(x)
for x in range (1,11,1):
    print(x)
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total:{total}")
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
num = [5,2,5,2,2]
for x in num:
    output = ""
    for y in range(x):
        output+="X"
    print(output)
names =['saim','Sam','waseem']
print(names)
print(names[2])
print(names[-1])
print(names[0:3])
numbers= [1,2,3,4,6,7,4,7,8,9]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(max)
matrix = [
    [1,2,3],
    [2,3,4],
    [1,2,4]
]
for row in matrix:
    for x in row:
        print(x)
# list function
num = [1,2,2,4,5,6]
num.append(5)
print(num)
num.insert(0,3)
print(num)
num.insert(0,5)
print(num)
num = [1,2,2,4,20,6]
print(num.index(2))
