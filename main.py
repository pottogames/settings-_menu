from tkinter import *
from tkinter import ttk
import os
import webbrowser



root = Tk()
root.geometry("370x575")
root.title("function menu!!!")

font='Helvetica 18 bold'

frm = ttk.Frame(root, padding=10)
frm.grid()



#def function!


#create new button 1 
def op1():
    0

#create new button 2
def op2():
    0

#create new button 2
def op3():
    0

#create new button 2
def op4():
    0

#create new button 2
def op5():
    0

#create new button 2
def op6():
    0
#create new function 7
def op7():
    0
#create new functiom 8
def op8():
    0
#create new function 9
def op9():
    0

def op10():
    0

def op11():
    0 

def op12():
    0

def op13():
    0

def op14():
    0

def op15():
    0

def op16():
    0

def op17(): 
    0


#def function url !


url = 'http://www.google.com'

def OpenUrl(url):
    webbrowser.open_new(url)

url2 = 'https://www.clocktab.com'

def OpenUrl(url2):
    webbrowser.open_new(url2)

 
op2 = Label(frm,text="Setting Menu!",background="green", font='Helvetica 18 bold').grid(column=1, row=1, rowspan=1, columnspan=10,pady=0)


op2 = Label(frm, text="Click Here To!").grid(column=6, row=3,)
op1 = Button(frm, text="send!", command=set, bg="green", fg="yellow").grid(column=8, row=3)

op5 = Label(frm, text="Click to Print!").grid(column=6, row=5,)
op6 = Button(frm, text="Print", bg="green", fg="yellow").grid(column=8, row=3)

op7 = Label(frm, text="Click here to sing-in👤").grid(column=6, row=4,)
op8 = Button(frm, text="Sing-in", bg="green", fg="yellow").grid(column=8, row=4,)

op9 = Label (frm, text="Click Here To Register!").grid(column=6, row=5,)
op10 =  Button (frm, text="Register", bg="green", fg="yellow").grid(column=8, row=5,)

op11 = Label (frm, text="Click Here To Play").grid(column=6, row=6)
op11 = Button (frm, text="Play now👩🏾‍💻", bg="green", fg="yellow").grid(column=8, row=6)

op12 = Label (frm, text="Click Here To Create A Clock!").grid (column=6, row=7)
op13 = Button (frm, text="Click here to create a clock!", command=OpenUrl(url2), bg="green", fg="yellow").grid (column=8, row=7)

op14 = Label (frm, text="Click Here To Open settings").grid (column=6, row=8)
op15 = Button (frm, text="Open Settings", bg="green", fg="yellow").grid (column=8, row=8)

op16 = Label (frm, text="Click Here To Create a New Folder").grid (column=6, row=9)
op17 = Button (frm, text="📁New Folder📁", bg="green", fg="yellow").grid (column=8, row=9)

op16 = Label (frm, text="Click Here To Open Google").grid (column=6, row=8)
op17 = Button (frm, text="open Google🌐", bg="green", command=OpenUrl(url),fg="yellow").grid (column=8, row=8)
op16 = Label (frm, text="Click Here To Open WI-FI Settisgs!").grid (column=6, row=10)
op17 = Button (frm, text="open WI-FI⚡", bg="green", fg="yellow").grid (column=8, row=10)

op17 = Label   (frm, text="Create A New image").grid (column=6, row=11)
op17 = Button  (frm, text="Create image", bg="green", fg="yellow").grid (column=8, row=11)

op12 = Label  (frm, text = "Click Here To Open calculator!").grid(column=6, row=12)
op14 = Button (frm, text = "Open calculator!",bg="green",fg="yellow").grid(column=8, row=12)

op12 = Label  (frm, text = "Click Here To Open amazon!").grid(column=6, row=13)
op14 = Button (frm, text = "Open amazon🌐",bg="green",fg="yellow").grid(column=8, row=13)

op12 = Label  (frm, text = "Click Here To Open AliExpress!").grid(column=6, row=14)
op14 = Button (frm, text = "Open AliExpress🌐",bg="green",fg="yellow").grid(column=8, row=14)

op12 = Label  (frm, text = "Click Here To Open ebay🌐").grid(column=6, row=15)
op14 = Button (frm, text = "Open ebay!",bg="green",fg="yellow").grid(column=8, row=15)

op12 = Label  (frm, text = "Click Here To Open function manager!").grid(column=6, row=16)
op14 = Button (frm, text = "Open function manager!",bg="green",fg="yellow").grid(column=8, row=16)

op12 = Label  (frm, text = "Click Here To Open spotify!").grid(column=6, row=17)
op14 = Button (frm, text = "Open spotify!",bg="green",fg="yellow").grid(column=8, row=17)

op12 = Label  (frm, text = "Click Here To Open youtube").grid(column=6, row=18)
op14 = Button (frm, text = "Open youtube!",bg="green",fg="yellow").grid(column=8, row=18)

op12 = Label  (frm, text = "Click Here To Open chanel youtube").grid(column=6, row=19)
op14 = Button (frm, text = "Open chanel youtube!",bg="green",fg="yellow").grid(column=8, row=19)

op3 = Label(frm, text="Click Here  To Exit!").grid(column=6, row=20)
op4 = Button(frm, text="Quit", command=root.destroy, bg="green", fg="yellow").grid(column=8, row=20,)

#END LABEL
op3 = Label(frm, text="*all copyright to be saved to pottogames!").grid(column=6, row=22)



#mainlooped!
root.mainloop()
