from os import *
import os,sys
from os import link
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  
from googletrans import Translator
from tkinter import messagebox
import webbrowser
import speech_recognition as sr
import pyttsx3


root = tk.Tk()
root.title('Translate Life ')
root.geometry('1280x680')
root.maxsize(1280,680)
root.minsize(1280,680)

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

def translate():
        language_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if language_1 == '':
                messagebox.showerror('Translate Life','please fill the box')
        else:
                t2.delete(1.0,'end')
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                t2.insert('end',output.text)

def clear():
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')

def reconocimiento_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es")  # Reconocimiento de voz en español
            print("Has dicho: " + texto)
            t1.delete(1.0, 'end')
            t1.insert('end', texto)

            cl = choose_langauge.get()
            if cl != 'Seleccione Idioma':
                translator = Translator()
                traduccion = translator.translate(texto, dest=cl)  # Traducción al idioma seleccionado
                t2.delete(1.0, 'end')
                t2.insert('end', traduccion.text)
            else:
                messagebox.showerror('Translate Life', 'Por favor, seleccione un idioma')

        except sr.UnknownValueError:
            print("No se pudo reconocer el habla.")
        except sr.RequestError as e:
            print("Error en la solicitud: {0}".format(e))

def reproducir():
    texto_traducido = t2.get("1.0", "end-1c")
    if texto_traducido != '':
        engine = pyttsx3.init()
        
        # Configuración de la voz y velocidad
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Cambia el índice para seleccionar la voz deseada
        engine.setProperty('rate', 130)  # Cambia el valor para ajustar la velocidad (100 es el valor predeterminado)
        
        engine.say(texto_traducido)
        engine.runAndWait()
    else:
        messagebox.showerror('Translate Life', 'No hay traducción para reproducir')


img = ImageTk.PhotoImage(Image.open('img/Fondo2.png'))
panel = tk.Label(root, image = img)
panel.pack(fill = "both", expand = "yes")

a = tk.StringVar() 
auto_detect = ttk.Combobox(root, width = 18, textvariable = a, state='readonly',font=('Bahnschrift SemiCondensed',16,'normal'),) 

auto_detect['values'] = (
                          'Deteccion automatica', 
                          ) 
  
auto_detect.place(x=533,y=250)
auto_detect.current(0) 

l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 18, textvariable = l, state='readonly',font=('Bahnschrift SemiCondensed',16,'normal')) 
  
def link():
        webbrowser.open("http://translate_life_ia.test/")
def espa():
        webbrowser.open("https://drive.google.com/file/d/10reW64T7xSGkTkiIeJ_xl6ecQkQM4Ils/view?usp=drive_link")
def en():
        webbrowser.open("https://drive.google.com/file/d/1ZPVH5KLuoL8cKiZxLtOSqi52IlCtcZeq/view?usp=drive_link")
def ru():
        webbrowser.open("https://drive.google.com/file/d/1AGPMKeHhe31gd1caCaon4onWfLHmtd6Z/view?usp=sharing")
def ja():
        webbrowser.open("https://drive.google.com/file/d/1Eyz5b0DFVX0-fMiCNjxPuUC1m5MqVQrG/view?usp=sharing")
def pag():
        webbrowser.open("http://translate_life_ia.test/#contactanos")


choose_langauge['values'] = (
                        'Seleccione Idioma', 
                        'Afrikaans',
                        'Albanian',
                        'Arabic',
                        'Armenian',
                        'Azerbaijani',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                        'Catalan',
                        'Cebuano',
                        'Chichewa',
                        'Chinese (simplified)',
                        'Chinese (traditional)',
                        'Corsican',
                        'Croatian',
                        'Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Haitian Creole',
                        'Hausa',
                        'Hawaiian',
                        'Hebrew',
                        'Hindi',
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'Korean',
                        'Kurdish (kurmanji)',
                        'Kyrgyz',
                        'Lao',
                        'Latin',
                        'Latvian',
                        'Lithuanian',
                        'Luxembourgish',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Nepali',
                        'Norwegian',
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Scots Gaelic',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa',
                        'Yiddish',
                        'Yoruba',
                        'Zulu',
                          ) 
  
choose_langauge.place(x=533,y=350)
choose_langauge.current(0) 


t1 = Text(root,width=50,height=30,borderwidth=7,relief=RIDGE)
t1.place(x=100,y=100)

t2 = Text(root,width=50,height=30,borderwidth=7,relief=RIDGE)
t2.place(x=745,y=100)


button = Button(root,text="Traducir",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',20,'normal'),cursor="hand2",command=translate)
button.place(x=275,y=600)

boton_hablar = Button(root, text="Hablar", relief=RIDGE, borderwidth=3, font=('Bahnschrift SemiCondensed', 20, 'normal'), cursor="hand2", command=reconocimiento_voz)
boton_hablar.place(x=150, y=600)

boton_reproducir = Button(root, text="Reproducir", relief=RIDGE, borderwidth=3, font=('Bahnschrift SemiCondensed', 20, 'normal'), cursor="hand2", command=reproducir)
boton_reproducir.place(x=700, y=600)

clear = Button(root,text="Limpiar",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',20,'normal'),cursor="hand2",command=clear)
clear.place(x=580,y=600)

link = Button(root,text="Opiniones",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',20,'normal'),cursor="hand2",command=link)
link.place(x=855,y=600)

banner = Image.open('img/banner.png')
banner = ImageTk.PhotoImage(banner)
es = Button(root,relief=RIDGE,image=banner,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=pag)
es.place(x=280,y=5)


img1 = Image.open('img/espanol.png')
img1 = ImageTk.PhotoImage(img1)
espa = Button(root,relief=RIDGE,image=img1,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=espa)
espa.place(x=28,y=120)

img2 = Image.open('img/ingles.png')
img2 = ImageTk.PhotoImage(img2)
en = Button(root,relief=RIDGE,image=img2,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=en)
en.place(x=28,y=200)

img3 = Image.open('img/japon.png')
img3 = ImageTk.PhotoImage(img3)
ja = Button(root,relief=RIDGE,image=img3,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=ja)
ja.place(x=28,y=280)

img4 = Image.open('img/ruso.png')
img4 = ImageTk.PhotoImage(img4)
ru = Button(root,relief=RIDGE,image=img4,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=ru)
ru.place(x=28,y=360)

root.mainloop()