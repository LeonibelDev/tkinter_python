import sys
from tkinter import messagebox
from tkinter import *
from circulo import *

def exit_sys():
    exit_msg = messagebox.askquestion("Confirmar La Salida", "Estas seguro que deseas salir")

    if exit_msg == 'yes':
        print('App closed successfull')
        return sys.exit()
        
    if exit_msg == 'no':
        return print('open')

circulo()