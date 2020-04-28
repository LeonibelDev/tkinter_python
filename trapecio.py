from tkinter import ttk
from tkinter import *

def trapecio():
    class comp2:
    
        def __init__(self, window):
          
            self.wind = window
            self.wind.title('Products Application by: @LeoDev')
            self.wind.geometry('400x360')
    
            self.wind.config(bg='#000A20', pady=10, padx=50)
           
            frame = LabelFrame(self.wind, text = 'CARCULAR AREA DE UN TRAPECIO')
            frame.grid(row = 0, column = 3, columnspan = 6, pady = 20)
    
            Label(frame, text = 'ALTURA DEL TRAPECIO: ').grid(row = 1, column = 0)
            self.num1 = Entry(frame)
            self.num1.focus()
            self.num1.grid(row = 1, column = 1, pady = 10, padx = 10)
    
            Label(frame, text = 'A / BASE MAYOR: ').grid(row = 2, column = 0)
            self.num2 = Entry(frame)
            self.num2.grid(row = 2, column = 1, pady = 10, padx = 10)
            
            Label(frame, text = 'B / BASE MENOR: ').grid(row = 3, column = 0)
            self.num3 = Entry(frame)
            self.num3.grid(row = 3, column = 1, pady = 10, padx = 10)
           
            ttk.Button(frame, text = 'CALCULAR', command = self.comp).grid(row = 6, columnspan = 2, sticky = W + E)
            ttk.Button(frame, text = 'LIMPIAR', command = self.clear).grid(row = 7, columnspan = 2, sticky = W + E)
            
            self.message = Label(text = '', fg = '#fff', background = "#006", font=36)
            self.message.grid(row = 8, column = 3, columnspan = 6, sticky = W + E)
    
                
        def comp(self):
            self.message['text'] = "El area es de {}".format(int(self.num1.get()) * ((int(self.num2.get()) + int(self.num3.get())) / 2))                
        
        def clear(self):
            self.num1.delete(0, END)
            self.num2.delete(0, END)
            self.num3.delete(0, END)   
            self.message['text'] = "" 
            
    if __name__ == '__main__':
        window = Tk()
        application = comp2(window)
        window.mainloop()

def start_trapecio():
    trapecio()
   