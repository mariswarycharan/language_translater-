from msilib.schema import ComboBox
from optparse import Values
from tkinter.ttk import Combobox
from turtle import color, width
import googletrans
from tkinter import *
from tkinter.font import BOLD, ITALIC
from translate import Translator
from fnmatch import translate

from pyparsing import col

# from matplotlib.ft2font import BOLD



root = Tk()


language = googletrans.LANGUAGES
list = []
for i in language:
    list.append(language[i])

root.title("XO_game")
root.configure(background="#33ccff")
title = Label(root,text="language translater",font = ("ALGERIAN",40,BOLD,ITALIC), foreground="red",background="black",padx=10,pady=20)
title.grid(row=1,column=2)

l1 = Label(root,padx=220,background="#33ccff")
l1.grid(row=1,column=1)

# "----------------------------------left-----------------------------------------"

l1 = Label(root,padx=220,pady=30,background="#33ccff")
l1.grid(row=2,column=1)


monthbox = Combobox(root,width=20,font = ("ALGERIAN",20,ITALIC), foreground="red",background="black")
monthbox['values'] = list
monthbox.grid(row = 3,column = 1)
monthbox.set("english")
monthbox.current()

l1 = Label(root,padx=220,pady=10,background="#33ccff")
l1.grid(row=4,column=1)

lan_left = Label(root,font = ("ALGERIAN",30,ITALIC),background="red",padx=10,borderwidth=10)
lan_left.grid(row=5,column=1)

photo_translate = PhotoImage(file="C:\\Users\\USER\\Downloads\\translator.png")
l_ima = Label(root,image=photo_translate)
l_ima.grid(row=2,column=2,rowspan=4)



def main_left():
    global get_left
    get_left = monthbox.get()
    lan_left.configure(text=get_left)
    lan_left.after(1,main_left)
    
main_left()


text_box_left = Text(root,width=55,height=20)
text_box_left.grid(row=6,column=1)

input_lan = str(text_box_left.get(1.0,END))

# "----------------------------------right-----------------------------------------"
l1 = Label(root,padx=220,pady=30,background="#33ccff")
l1.grid(row=2,column=3)


monthbox_r = Combobox(root,width=20, font = ("ALGERIAN",20,ITALIC),foreground="red",background="black")
monthbox_r['values'] = list
monthbox_r.grid(row = 3,column = 3)
monthbox_r.set("select language")
monthbox_r.current()

l1 = Label(root,padx=220,pady=10,background="#33ccff")
l1.grid(row=4,column=3)

lan_right = Label(root,padx=10,font = ("ALGERIAN",30,ITALIC),background="red",borderwidth=10)
lan_right.grid(row=5,column=3)

def main_right():
    
    global get_right
    get_right = monthbox_r.get()
    lan_right.configure(text=get_right)
    lan_right.after(1,main_right)

    
main_right()



text_box_right = Text(root,width=55,height=20,font=("arial",10))
text_box_right.grid(row=6,column=3)

result_lan = text_box_right.get(1.0,END)



def main():
    
    global input_lan,get_left,get_right
    
    input_lan = str(text_box_left.get(1.0,END))
    
    print(get_left)
    print(get_right)
    print(input_lan)
    
    translator= Translator( from_lang=get_left, to_lang=get_right)
    translation = translator.translate(input_lan)
    # print(translation)
    text_box_right.insert(END,translation)
    
    
# main()

button_translate = Button(root,padx=50,text="translate", foreground="red",background="#33ff33",font = ("ALGERIAN",20,ITALIC),pady=10,command=main)
button_translate.grid(row=6,column=2)

def remove():
    text_box_right.delete(1.0,END)


button_remove = Button(root,padx=50,text="""remove text in 
box""",font = ("ALGERIAN",20,ITALIC), foreground="red",background="#33ff33",command=remove)
button_remove.grid(row=7,column=2)



root.mainloop()