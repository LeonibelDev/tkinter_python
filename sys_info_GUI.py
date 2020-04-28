#_autor_ @leoDev
#_verison_ 0.0.1
#2020

# MODULES
from circulo import *
from compara_2_num import *
from compara_3_num import *
from trapecio import *
from triangulo import *
# MODULES

from tkinter import ttk 
from tkinter import *
import sys, platform, os, socket, math
from action import * 
from sys_info import *
from calc import *  
import tkinter as tk
from PIL import ImageTk ,Image

def consola_true():

    root = tk.Tk()
    root.geometry('600x560')
    root.title('')
    root.config(bg='#000A20', pady=10, padx=10)
    # _photo = tk.PhotoImage(file = "./kevin-zalazar-Cax2udvMujc-unsplash.jpg")
    
    # MENU
    
    menu_general = Menu(root) #incrustamos un menu en la root, aunque todabia no es visible
    root["menu"] = menu_general #hacemos que la root tenga de menu a "menu_general"
    
    #MENU ARCHIVO

    menu_archivo = Menu(menu_general)
    menu_archivo.add_separator()
    # CALCULO
    
    calculo = Menu(menu_general)
    calculo.add_command(label = "Trapecio", command=start_trapecio)
    calculo.add_command(label = "Triangulo", command=triangulo)
    calculo.add_command(label = "Circulo", command=circulo)
    
    menu_archivo.add_cascade(label = "Area", menu = calculo)

    # COMPARACION 

    comparacion = Menu(menu_general)
    comparacion.add_command(label = "Compara 2 numeros", command=init_comp_two)
    comparacion.add_command(label = "Compara 3 numeros")
    menu_archivo.add_cascade(label = "Comparacion", menu = comparacion)
    menu_archivo.add_command(label = 'Calculadora', command= calculator)
    menu_archivo.add_command(label = 'Promedio', command= calculator)
    menu_archivo.add_command(label = 'Factura')

    menu_general.add_cascade(label = "Archivo", menu = menu_archivo)
    
    menu_archivo.add_command(label = "Salir", command = root.destroy)


    #MENU AYUDA

    menu_ayuda = Menu(menu_general)
    menu_ayuda.add_command(label = "Acerca de...")
    menu_general.add_cascade(label = "Ayuda", menu = menu_ayuda)
    
    menu_general.add_command(label = "Salir", command = root.destroy)

    # -------------------------------------------------------------------------

    # LOGO
    # Myframe = Frame(root)
    # Myframe.pack(fill="both", expand=True)
    # Imagen=PhotoImage(file="logo.png")
    # Imagen_2 =Label(Myframe, Image=Imagen)
    # Imagen_2.place(x=100, y=200)

    img=ImageTk.PhotoImage(Image.open ("logo.png"))
    lab=Label(image=img, bg='#000A20', height=260)
    lab.pack()


    var = StringVar()
    label = Label( root, textvariable=var, relief=RAISED, text="green", font=36, borderwidth=0, pady = 12, bg='#000A20', fg="#fff")
    var.set("Liceo Tecnico Profesional Jose Francisco Bobadilla\n Calle Cesar E. Crispin #\n ``Educando en valores y competencias para la vida en la sociedad``")
    label.pack()
    root.mainloop()

    return root
consola_true()