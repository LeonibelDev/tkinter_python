from tkinter import ttk
from tkinter import *

def triangulo():
    class comp2:
    
        def __init__(self, window):
          
            self.wind = window
            self.wind.title('Products Application by: @LeoDev')
            self.wind.geometry('400x360')
    
            self.wind.config(bg='#000A20', pady=10, padx=50)
           
            frame = LabelFrame(self.wind, text = 'CARCULAR AREA DE UN TRIANGULO')
            frame.grid(row = 0, column = 3, columnspan = 6, pady = 20)
    
            Label(frame, text = 'BASE DEL TRIANGULO: ').grid(row = 1, column = 0)
            self.num1 = Entry(frame)
            self.num1.focus()
            self.num1.grid(row = 1, column = 1, pady = 4, padx = 10)
    
            Label(frame, text = 'ALTURA DEL TRIANGULO: ').grid(row = 2, column = 0)
            self.num2 = Entry(frame)
            self.num2.grid(row = 2, column = 1, pady = 4, padx = 10)
    
            Label(frame, text = 'MEDIDA: ').grid(row = 3, column = 0)
            self.num3 = Entry(frame)
            self.num3.grid(row = 3, column = 1, pady = 4, padx = 10)
    
            ttk.Button(frame, text = 'CALCULAR', command = self.comp).grid(row = 4, columnspan = 2, sticky = W + E)
            ttk.Button(frame, text = 'LIMPIAR', command = self.clear).grid(row = 5, columnspan = 2, sticky = W + E)
        
            self.message = Label(text = '', fg = '#fff', background = "#006", font=36)
            self.message.grid(row = 5, column = 3, columnspan = 6, sticky = W + E)
    
          
        
        def comp(self):
            self.message['text'] = "El area es de {}{}".format((1/2 * (int(self.num1.get()) * int(self.num2.get()))), str( self.num3.get()))                
        
        def clear(self):
            self.num1.delete(0, END)
            self.num2.delete(0, END)
            self.message['text'] = ""
            
    if __name__ == '__main__':
        window = Tk()
        application = comp2(window)
        window.mainloop()
