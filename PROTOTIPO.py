from os import link
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  
from googletrans import Translator
from tkinter import messagebox
import webbrowser

root = tk.Tk()
root.title('PROTO - Translate Life ')
root.geometry('500x300')
root.maxsize(500,300)
root.minsize(500,300)


def translate():
        language_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if language_1 == '':
                messagebox.showerror('Translate Life','Llena el Cuadro')
        else:
                t2.delete(1.0,'end')
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                t2.insert('end',output.text)

def clear():
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')

a = tk.StringVar() 
auto_detect = ttk.Combobox(root, width = 18, textvariable = a, state='readonly',font=('Bahnschrift SemiCondensed',16,'normal'),) 

auto_detect['values'] = (
                          'Deteccion automatica', 
                          ) 
  
auto_detect.place(x=0,y=0)
auto_detect.current(0) 

l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 18, textvariable = l, state='readonly',font=('Bahnschrift SemiCondensed',16,'normal')) 
  
def link():
        webbrowser.open("http://127.0.0.1:8080")

choose_langauge['values'] = (
                        'Selecciona El Idioma',      
                        'Spanish',
                        'English',
                          ) 
  
choose_langauge.place(x=230,y=0)
choose_langauge.current(0) 


t1 = Text(root,width=25,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=0,y=50)

t2 = Text(root,width=25,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=230,y=50)


button = Button(root,text="Traducir",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',15,'normal'),cursor="hand2",command=translate)
button.place(x=0,y=250)


clear = Button(root,text="Limpiar",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',15,'normal'),cursor="hand2",command=clear)
clear.place(x=100,y=250)

link = Button(root,text="Opiniones",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',15,'normal'),cursor="hand2",command=link)
link.place(x=200,y=250)
root.mainloop()