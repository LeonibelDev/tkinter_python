import tkinter as tk
import sys

def calculator():
    calc = tk.Tk()
    calc.title("Calculator")
   
    buttons = [
    '1',  '2',  '3',  '*',  'C',
    '4',  '5',  '6',  '/',  '-',  
    '7',  '8',  '9',  '+',  '.',  
    '0',  '=' 
    ]
    
    # set up GUI
    calc.config(bg='#000A20', pady =10, padx=10)
    
    row = 1
    col = 0
    for i in buttons:
        button_style = 'raised'
        action = lambda x = i: click_event(x)
        tk.Button(calc, text = i, width = 4, height = 4, relief = button_style, command = action) \
            .grid(row = row, column = col, sticky = 'nesw')
        col += 1
        if col > 4:
            col = 0
            row += 1   
    
    exit = tk.Button(calc, text = 'Cerrar', width = 6, height = 2, command = calc.destroy)
    exit.grid(column = 2, row = 4)

    display = tk.Entry(calc, width = 40, bg = "white", font = 150)
    display.grid(row = 0, column = 0, columnspan = 5, pady=10)

    def click_event(key):
    
        if key == '=':
            if '/' in display.get() and '.' not in display.get():
                display.insert(tk.END, ".0")
            try:
                result = eval(display.get())
                display.insert(tk.END, " = " + str(result))
                print(result)
            except:
                display.insert(tk.END, "   Error, use only valid chars")
                
        elif key == 'C':
            display.delete(0, tk.END)
            
            
        elif key == '$':
            display.delete(0, tk.END)
            display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")
            
    
        elif key == '@':
            display.delete(0, tk.END)
            display.insert(tk.END, "wwwwwwwwwwwwwwwwebsite")        
    
            
        elif key == 'neg':
            if '=' in display.get():
                display.delete(0, tk.END)
            try:
                if display.get()[0] == '-':
                    display.delete(0)
                else:
                    display.insert(0, '-')
            except IndexError:
                pass
    
        else: 
            if '=' in display.get():
                display.delete(0, tk.END)
            display.insert(tk.END, key)
    
    calc.mainloop()