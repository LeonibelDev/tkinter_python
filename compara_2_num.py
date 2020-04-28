from tkinter import ttk
from tkinter import *

def init_comp_two():
    class comp2:
    
        def __init__(self, window):
          
            self.wind = window
            self.wind.title('Products Application by: @LeoDev')
            self.wind.geometry('300x360')
    
            self.wind.config(bg='#000A20', pady=10, padx=40)
           
            # Creating a Frame Container
            frame = LabelFrame(self.wind, text = 'COMPARA DOS NUMEROS')
            frame.grid(row = 0, column = 6, columnspan = 6, pady = 30)
    
            Label(frame, text = 'Numero 1: ').grid(row = 1, column = 0)
            self.num1 = Entry(frame)
            self.num1.focus()
            self.num1.grid(row = 1, column = 1, pady = 10, padx = 10)
    
            Label(frame, text = 'Numero 2: ').grid(row = 2, column = 0)
            self.num2 = Entry(frame)
            self.num2.grid(row = 2, column = 1, padx = 10)
    
            ttk.Button(frame, text = 'COMPARAR', command = self.comp).grid(row = 3, columnspan = 2, sticky = W + E)
            ttk.Button(frame, text = 'LIMPIAR', command = self.clear).grid(row = 4, columnspan = 2, sticky = W + E)
            
            self.message = Label(text = '', fg = '#fff', background = "#006", font=36)
            self.message.grid(row = 3, column = 6, columnspan = 6, sticky = W + E)
    
          
        
        def comp(self):
            if int(self.num1.get()) > int(self.num2.get()):
                self.message['text'] = "El numero {} es mayor que el {} ".format(self.num1.get(), self.num2.get())                
                
            else:
                self.message['text'] = "El numero {} es mayor que {} ".format(self.num2.get(), self.num1.get())                
        
        def clear(self):
            self.num1.delete(0, END)
            self.num2.delete(0, END) 
            self.message['text'] = ""

    if __name__ == '__main__':
        window = Tk()
        application = comp2(window)
        window.mainloop()
