# exception : events detected during the execution that interrupts the flow of program.
try:
    numerator = int(input("Enter a number: "))
    denominator = int(input("Enter a number: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("you are divide by 0!, idiot!")
except ValueError as e:
    print(e)
    print("Enter only Number Plz")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute! ")
import os
path = "give your path of directory"

if os.path.exists(path):
    print("That Location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is the directory!")
else:
    print("That location doesn't exists!")
with open('python script.txt') as file:
    print(file.read())
try:
    with open('python script.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
text = "my name is sam!"
with open('python script.txt','a') as file:
    file.write(text)
import shutil
shutil.copyfile("python script.txt","copy.txt")
print(file.close())
import os

source = "python script.txt"
destination = 'give your path of directory or file'
try:
    if os.path.exists(destination):
        print("The file is already exists!")
    else:
        os.replace(source,destination)
        print(source,"was moved")
except FileNotFoundError:
    print(source,"was not found")
import os
import shutil
path = 'folder'
path = "copy.txt"
path = "empty_name"
try:
    os.remove(path) # delete file
    os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("The file is not found:(")
except PermissionError:
    print("You have not permission to delete file.")
else:
    print(path,"was delete")
