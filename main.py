"""
import tkinter as tk

gui = tk.Tk()
gui.geometry('500x500')
lb = tk.Listbox(height='30', width='50')
lb.insert(0, "First")
lb.insert(1, "Second")
lb.insert(2, "Third")


def click(i):
    if i == 1:
        if variable[0].get() == 1:
            print("First Checkbox")
    elif i == 2:
        if variable[1].get() == 1:
            print("Second Checkbox")
    elif i == 3:
        if variable[2].get() == 1:
            print("Third checkbox")


def click_too(event):
    cs = lb.curselection()
    for i in cs:
        if i == 0:
            print("First Listbox")
        elif i == 1:
            print("Second Listbox")
        elif i == 2:
            print("Third Listbox")


variable = []
for i in range(3):
    var = tk.IntVar()
    variable.append(var)
ck_1 = tk.Checkbutton(text="First", variable=variable[0], command=lambda: click(1))
ck_2 = tk.Checkbutton(text="Second", variable=variable[1], command=lambda: click(2))
ck_3 = tk.Checkbutton(text="Third", variable=variable[2], command=lambda: click(3))
lb.bind("<Double-1>", click_too)
lb.place(x=0, y=10)
ck_1.place(x=350, y=100)
ck_2.place(x=350, y=200)
ck_3.place(x=350, y=300)
gui.mainloop()
"""

"""
import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.geometry('500x500')
lb = tk.Label(text='Color')
bt = tk.Button(text = 'Click')

def click():
    bt.configure(text = f'Color is {cb.get()}')
    print(cb.get())
x = tk.StringVar()
cb = ttk.Combobox(gui, values=['red', "green", "yellow"],textvariable = x)
lb.pack(side='top')
bt.configure(command = click)
cb.current()
cb.pack(side='top')
bt.pack(side = 'top')
gui.mainloop()
"""

"""
import tkinter as tk
from tkinter import ttk
gui = tk.Tk()
gui.geometry('500x500')
def click(eventObject):
    print(var.get())
var = tk.StringVar()
cb = ttk.Combobox(values = ["Acres","Ft"],textvariable = var)
cb.bind("<<ComboboxSelected>>",click)
cb.current(0)
cb.pack(side='top')
gui.mainloop()
"""

"""
import tkinter as tk
from tkinter import ttk
gui = tk.Tk()
def click():
    lb.configure(bg = var.get())
    bt1.configure(bg = var.get())

def click_too():
    lb.configure(bg = 'white')
    bt1.configure(bg = 'white')
var = tk.StringVar()
lb = tk.Label(text = 'Languages')
cb = ttk.Combobox(values = ["red","green","violet"],textvariable = var)
bt1 = tk.Button(text = 'Click',command = click)
bt2 = tk.Button(text = 'Default',command = click_too)
cb.current(0)
lb.pack(side = 'top')
cb.pack(side = 'top')
bt1.pack(side = 'top')
bt2.pack(side = 'top')

gui.mainloop()
"""

"""
import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.geometry('500x500')
def click(event):
    lb.configure(text = cb.get())

lb = tk.Label(text = 'Yet to start')
cb = ttk.Combobox(values = [i for i in range(1,10)])
cb.bind("<<ComboboxSelected>>",click)
lb.pack(side = 'top')
cb.pack(side = 'top')
gui.mainloop()
"""

"""
import tkinter as tk

gui = tk.Tk()
fr1 = tk.Frame().pack()
fr2 = tk.Frame().pack(side = 'bottom')

def click(bt):
    print("You got", bt['text'])


bt1 = tk.Button(fr1, text='First', command=lambda: click(bt1))
bt2 = tk.Button(fr1, text='Second', command=lambda: click(bt2))
bt3 = tk.Button(fr2, text='Winner', command=lambda: click(bt3))
bt4 = tk.Button(fr2, text='Runner', command=lambda: click(bt4))
bt1.pack(side = 'left')
bt2.pack(side = 'left')
bt3.pack(side = 'bottom')
bt4.pack(side = 'bottom')

gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
fr = tk.Frame().pack(side = 'top')
def click():
    tl = tk.Toplevel()
    tl.geometry('500x500')
    tl.mainloop()
bt = tk.Button(fr,text = 'click',command = click)
bt.pack(side = 'top')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('200x140')
color = ['violet','indigo','blue','green','yellow','orange','red']
for i in color:
    fr = tk.Frame(height = 20,width = 640,bg = i).pack()
gui.mainloop()
"""

"""
import tkinter as tk

gui = tk.Tk()
lb = tk.Label(gui, text='image')
fr = tk.Frame().pack()
img = tk.PhotoImage(file='index.png')
lbl = tk.Label(gui,image = img)
lbl.pack()
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
fr1 = tk.Frame(bg = 'green',height = '100',width = '100').grid(row = 1,column = 0)
fr2 = tk.Frame(bg = 'blue',height = '100',width = '100').grid(row = 1,column = 1)
fr3 = tk.Frame(bg = 'yellow',height = '100',width = '100').grid(row = 0,column = 0)
fr4 = tk.Frame(bg = 'cyan',height = '100',width = '100').grid(row = 0,column = 1)

gui.mainloop()
"""

"""
import tkinter as tk

gui = tk.Tk()
gui.geometry('500x500')


def click():
    print("Hey mister")


fr1 = tk.Frame().pack(side='top')
fr2 = tk.Frame().pack(side='bottom')
lb = tk.Label(fr1, text='Label')
bt = tk.Button(fr2, text='Click', command=click)
lb.pack(side = 'top')
bt.pack(side = 'bottom')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
fr = tk.Frame(gui).pack()
lb1 = tk.Label(fr,text = 'sunken',relief ='sunken').pack(side = 'left')
lb2 = tk.Label(fr,text = 'ridge',relief ='ridge').pack(side = 'left')
lb3 = tk.Label(fr,text = 'groove',relief ='groove').pack(side = 'left')
lb4 = tk.Label(fr,text = 'flat',relief ='flat').pack(side = 'left')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
fr1 = tk.Frame(gui,bg = 'red',width = '100',height = '100').pack(side = 'top')
fr2 = tk.Frame(gui,bg = 'blue',width = '50',height = '50').pack(side = 'top')
fr3 = tk.Frame(gui,bg = 'yellow',width = '25',height = '25').pack(side = 'top')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
fr1 = tk.Frame(gui,bg = 'red',width = '100',height = '100').pack(side = 'left')
fr2 = tk.Frame(gui,bg = 'blue',width = '100',height = '100').pack(side = 'left')
fr3 = tk.Frame(gui,bg = 'yellow',width = '100',height = '100').pack(side = 'left')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
def add_text():
    txt = en1.get() + " " + en2.get() + " " + en3.get()
    lbt.insert('end',f'{txt}\n')
    en1.delete('0','end')
    en2.delete('0', 'end')
    en3.delete('0', 'end')

def del_text():
    lbt.delete('active')

def up_text():
        updated = en1.get() + " " + en2.get() + " " + en3.get()
        idx = lbt.curselection()
        lbt.delete('active')
        lbt.insert(idx,f'{updated}\n')
lb1 = tk.Label(text = 'First name')
lb1.place(x = 50,y = 50)
lb2 = tk.Label(text = 'Last name')
lb2.place(x = 50,y = 70)
lb3 = tk.Label(text = 'Number').place(x = 50,y = 90)
en1 = tk.Entry()
en2 = tk.Entry()
en3  =tk.Entry()
lbt = tk.Listbox(width = '40',height = '10')
bt1 = tk.Button(text = 'Add',command = add_text)
bt2 = tk.Button(text = 'Delete',command = del_text)
bt3 = tk.Button(text = 'Update',command = up_text)
bt4 = tk.Button(text = 'Refresh',command = add_text)
lbt.insert(0,"Srivatsan T 8610593033")
lbt.insert(1,"Vignesh S 8610593033")
lbt.insert(2,"Girija S 9942381088")
en1.place(x = 150,y = 50)
en2.place(x = 150,y = 70)
en3.place(x = 150,y = 90)
lbt.place(x = 50,y = 150)
bt1.place(x = 50,y = 120)
bt2.place(x = 90,y = 120)
bt3.place(x = 140,y = 120)
bt4.place(x = 190,y = 120)

gui.mainloop()
"""

"""
import tkinter as tk

gui = tk.Tk()
for i in range(3):
    fr = tk.Frame().grid(row = i,column = 0)
    for j in range(3):
        l = tk.Label(fr,text = f"[{i}][{j}]",width = '10',height ='5').grid(row = i,column = j)
gui.mainloop()
"""

"""
import tkinter as tk
import random
gui = tk.Tk()
gui.geometry('500x500')
def click():
    print(random.randint(0,100))
lbf = tk.LabelFrame(gui,text = 'Random Value Generator',fg = 'red').pack(side = 'top',expand = 'yes',fill = 'both')
bt = tk.Button(lbf,text = 'Click',command = click).place(y = 50,x = 50)
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
sc = tk.Scrollbar(gui)
mylist = tk.Listbox(gui,yscrollcommand = sc.set)
for i in range(100):
    mylist.insert(i,f"This is line {i}")
mylist.pack(side = 'left',fill = 'both')
sc.pack(side = 'right',fill = 'y')
sc.configure(command = mylist.yview)
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
sc = tk.Scrollbar(gui)
text = tk.Text(yscrollcommand = sc.set)
for i in range(1000):
    text.insert('end',f'This is line {i}\n')
sc.configure(command = text.yview)
sc.pack(side = 'right',fill = 'y')
text.pack(side = 'left',fill = 'both')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
sc = tk.Scrollbar(gui,orient = tk.HORIZONTAL)
text = tk.Text(gui,xscrollcommand = sc.set,wrap = 'none')
for i in range(1000):
    text.insert('end',f'This is line {i} ')
sc.configure(command = text.xview)
text.pack(side = 'top',fill = 'both')
sc.pack(side = 'bottom',fill = 'x')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
def click():
    print(var.get())
var = tk.DoubleVar()
sc = tk.Scale(variable = var)
bt = tk.Button(text = 'Click',command = click)
sc.pack(side = 'top')
bt.pack(side = 'top')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
def click():
    print(var1.get(),var2.get())
var1 = tk.DoubleVar()
var2 = tk.DoubleVar()
sc1 = tk.Scale(variable = var1)
sc2 = tk.Scale(variable = var2,orient = "horizontal")
bt = tk.Button(text = 'click',command = click)
sc1.place(x = 50,y = 0)
sc2.place(x = 0,y = 300)
bt.place(x = 100,y = 400)
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
def click():
    print(var1.get())
var1 = tk.DoubleVar()
sc1 = tk.Scale(gui,length = 500,from_ = 0,to = 20,orient = 'horizontal',tickinterval = '1',variable = var1)
sc1.pack(side = 'top')
bt = tk.Button(text = 'click',command = click).pack(side = 'top')
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
var1 = tk.DoubleVar()
def click1():
    print(var1.get())
def click2():
    print(en1.get())
bt1 = tk.Button(text = 'Click ME!',command = click1)
sc1 = tk.Scale(from_ = 0,to = 500,length = 350,variable = var1,orient = 'horizontal')
en1 = tk.Entry(width = '55')
bt2 = tk.Button(text = 'Entry Box',command = click2)
bt2.place(x = 250,y = 200)
en1.place(x = 100,y = 150)
sc1.place(x = 100,y = 100)
bt1.place(x = 250,y = 50)
gui.mainloop()
"""

"""
import tkinter as tk
gui = tk.Tk()
gui.geometry('500x500')
def click():
    tb.insert("end",str(sb.get()) + "\n")
sb = tk.Spinbox(gui,from_ = 0,to = 40,increment = 5)
tb = tk.Text()
bt = tk.Button(text = 'Click',command = click)
tb.pack(side = 'top')
sb.pack(side = 'top')
bt.pack(side = 'top')
gui.mainloop()
"""


import tkinter as tk
gui = tk.Tk()
