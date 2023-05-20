from sqlite3 import Row
import tkinter as tk 
from googletrans import Translator
from regex import F

win = tk.Tk()
win.title("Proto - Traductor")
win.geometry("200x70")

def translator():
    word = entry.get()
    translator = Translator()
    translation = translator.translate(word, dest = "es")
    label1=tk.Label(win, text=f'Traducir Palabra: {translation.text}', bg = "white")
    label1.grid(row=2, column=0)

label = tk.Label(win, text= "Escribe Aqui:")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

buttom = tk.Button(win, text = "Traducir", command = translator)
buttom.grid(row=1, column=1)

win.mainloop()

