from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Sami Bro First GUI")

icon = PhotoImage(file='images.png')
window.iconphoto(True, icon)
window.config(background="sky blue")

window.mainloop()
# LAbels

from tkinter import *

window = Tk()

photo = PhotoImage(file='images.png')

label = Label(window,text="hello world",font=('Arial',40,'bold'),
              fg = '#00FF00',
              bg = 'black',
              relief= RAISED,
              bd = 10,
              padx=20,
              pady= 20,
              image=photo,
              compound='bottom')
label.pack()

window.mainloop()
# Button in python

from tkinter import  *

count = 0
def click():
    global count
    count +=1
    print(count,"likes")
window = Tk()

photo = PhotoImage(file='download.png')

button = Button(window,
                text="click me:",
                command=click,
                font=("Algerian", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()

window.mainloop()
# Entry box for single line

from tkinter import  *

def submit():
    username = entry.get()
    print("Hello "+username)
    # entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry =Entry(window,
             font=("Time new romans",20),
             fg="#00FF00",
             bg="black",)
entry.insert(0,'Sammy')
entry.config(show='$')

entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

Delete = Button(window,text="delete",command=delete)
Delete.pack(side=RIGHT)

backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side=RIGHT)

window.mainloop()
# CheckButton

from tkinter import *

def display():
    if(x.get()):
        print("You agree!")
    else:
        print("you don't agree!")

window = Tk()

x = BooleanVar()
photo = PhotoImage(file='python.png')
check_button = Checkbutton(window,
                            text="I  agree to study Python",
                            variable=x,
                            onvalue=True,
                            offvalue=False,
                            command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='#00FF00',
                           activeforeground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')

check_button.pack()
window.mainloop()
# RADIO BUTTON
from tkinter import *

food = ["Pizza","juice","briyani"]

def order():
    if(x.get()==0):
        print("You order pizza")
    elif (x.get()==1):
        print("You order juice!")
    elif (x.get()==2):
        print("You order briyani!")
    else:
        print("huh?")

window = Tk()

pizzaimg = PhotoImage(file='download P.png')
juice = PhotoImage(file='juice.png')
briyani = PhotoImage(file='biryani.png')
foodImages = [pizzaimg,juice,briyani]

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio button
                              variable=x,       # groups radiobutton together if they share the
                              value=index,      # assigns each radiobutton a different values
                              padx=25,          # adds padding on x-axis
                              font=("Impact",50),
                              image=foodImages[index], # adds image
                              compound='left',           # adds image & text to left-side
                              indicatoron=0,            # eliminate circle indicator
                              width = 375,              # sets width of the radio button
                              command=order)            # sets command of radiobutton to function
    radiobutton.pack(anchor=W)
window.mainloop()
# SLIDING SCALE IN PYTHON

from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+"degree C")


window = Tk()

# Add photo of fire logo
# Add photo of cold logo
scale = Scale(window,from_=100,to=0,
              length=600,
              orient= VERTICAL,
              font=('Consolas',20),
              tickinterval = 10,
              # showvalue = 0,
              resolution=5,
              troughcolor='RED',
              fg='#00FF00',
              bg='black')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()
# LIST BOX
def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"burger")
listbox.insert(3,"soup")
listbox.insert(4,"fries")
listbox.insert(5,"cheezy roll")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()


window.mainloop()
# MESSAGE BOX
from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='This is an info message box',message='You are amazing')
    messagebox.showerror(title='Error:', message='something went wrong')
    # messagebox.showwarning(title='Warning',message='You have A problem!')
    if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the message'):
        print('you retired a thing!')
    else:
        print('you canceled thing!')
    if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
        print('I like cake too :)')
    else:
        print('Why do you not like cake? :(')
    answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    if answer== 'yes':
        print('I like pie too!')
    else:
        print('why do you not like pie?')
    answer = messagebox.askyesnocancel(title='yes no cancel',message='Do you like to code?',icon='info')
    if (answer==True):
        print('You like to code ')
    elif (answer==False):
        print('Then why are you watching a video on coding?')
    else:
        print('you have dodged the question ')

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()

window.mainloop()
# COLORCHOOSER MODULE
from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)


window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()
# TEXT AREA
from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink free",25),
            height=10,
            width=13,
            padx=20,
            pady=20,
            fg='purple')
text.pack()
button =Button(window,text='submit',command=submit)
button.pack()
window.mainloop()
# OPENFILE
from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\DilawarComputer\\Desktop",
                                          title='Sam file')
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\DilawarComputer\\Desktop",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All Files",".*"),
                                    ])
    filetext = str(text.get(1,0,END))
    filetext = input ("Enter some text I guess")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
# MENUBAR
from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut some text:")
def copy():
    print("You copy some text:")
def paste():
    print("You paste some text:")

window = Tk()

openImage = PhotoImage()
SaveImage = PhotoImage()
exitImage = PhotoImage()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("Mv Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()
# FRAMES
from tkinter import *

window = Tk()

frame = Frame(window,bg="black",bd=5,relief=SUNKEN)
frame.place(x=100,y=100)

Button(frame,text='S',font=('Arial',25),width=3).pack(side=TOP)
Button(frame,text='M',font=('Arial',25),width=3).pack(side=LEFT)
Button(frame,text='A',font=('Arial',25),width=3).pack(side=LEFT)
Button(frame,text='I',font=('Arial',25),width=3).pack(side=LEFT)

window.mainloop()
# New Window
from tkinter import *
def create_window():
    new_window = Toplevel()

old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()
