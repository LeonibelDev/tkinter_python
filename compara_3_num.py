from tkinter import ttk
from tkinter import *

def init_comp():
    class comp2:
    
        def __init__(self, window):
          
            self.wind = window
            self.wind.title('Products Application by: @LeoDev')
            self.wind.geometry('300x360')
    
            self.wind.config(bg='#000A20', pady=10, padx=50)

            frame = LabelFrame(self.wind, text = 'COMPARA DOS NUMEROS')
            frame.grid(row = 0, column = 6, columnspan = 6, pady = 20)
    
            Label(frame, text = 'Numero 1: ').grid(row = 1, column = 0)
            self.num1 = Entry(frame)
            self.num1.focus()
            self.num1.grid(row = 1, column = 1, pady = 10, padx = 4)
    
            Label(frame, text = 'Numero 2: ').grid(row = 2, column = 0)
            self.num2 = Entry(frame)
            self.num2.grid(row = 2, column = 1, padx = 10, pady = 4)
    
            Label(frame, text = 'Numero 3: ').grid(row = 3, column = 0)
            self.num3 = Entry(frame)
            self.num3.grid(row = 3, column = 1, padx = 10, pady = 4)

            ttk.Button(frame, text = 'COMPARAR', command = self.comp).grid(row = 4, columnspan = 2, sticky = W + E)
            ttk.Button(frame, text = 'LIMPIAR', command = self.clear).grid(row = 5, columnspan = 2, sticky = W + E)
            
            self.message = Label(text = '', fg = '#fff', background = "#006", font=36)
            self.message.grid(row = 5, column = 6, columnspan = 6, sticky = W + E)
    
          
        
        def comp(self):
            nums = [int(self.num1.get()), int(self.num2.get()), int(self.num3.get())]
            mayor = 0
            for x in range(0, len(nums)):
                if nums[x] > mayor:
                    mayor = nums[x]
            self.message['text'] = "El numero mayor es {}".format(mayor)
            
        def clear(self):
            self.num1.delete(0, END)
            self.num2.delete(0, END)    
            self.num3.delete(0, END)  
            self.message['text'] = ""

    if __name__ == '__main__':
        window = Tk()
        application = comp2(window)
        window.mainloop()
init_comp()