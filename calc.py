from tkinter import *
import math

c = 1

def click(value):
    global c
    ex = entry.get()
    ans = ''
    
    try:
        if value == '⌫':
            ex = ex[0:len(ex)-1]
            entry.delete(0, END)
            entry.insert(0, ex)
            return
        elif value == 'AC':
            entry.delete(0, END)
        elif value == '√x':
            ans = math.sqrt(eval(ex))
        elif value == 'π':
            ans = math.pi
        elif value == '2π':
            ans = 2 * (math.pi)
        elif value == 'cos':
            if ex.endswith('°'):
                ex = ex[0:len(ex)-1]
                ans = round(math.cos(math.radians(eval(ex))), 5)
            else: 
                ans = round(math.cos(eval(ex)), 5)
        elif value == 'sin':
            if ex.endswith('°'):
                ex = ex[0:len(ex)-1]
                ans = round(math.sin(math.radians(eval(ex))), 5)
            else: 
                ans = round(math.sin(eval(ex)), 5)
        elif value == 'tan':
            if ex.endswith('°'):
                ex = ex[0:len(ex)-1]
                ans = round(math.tan(math.radians(eval(ex))), 5)
            else: 
                ans = round(math.tan(eval(ex)), 5)  # Fixed: changed from 4 to 5 for consistency
        elif value == '1/x':
            ans = round(1/(eval(ex)), 4)
        elif value == 'e^x':
            ans = round(math.exp(eval(ex)), 4)
        elif value == 'x²':
            ans = round(eval(ex)**2, 4)
        elif value == 'n!':
            ans = round(math.factorial(int(eval(ex))), 4)  # Fixed: added int() for factorial
        elif value == 'log':
            ans = round(math.log10(eval(ex)), 4)  # Fixed: changed to log10 (common logarithm)
        elif value == 'ln':
            ans = round(math.log(eval(ex)), 4)  # Fixed: changed to natural log
        elif value == 'deg':
            ans = ex + '°'
            entry.delete(0, END)  # Fixed: clear first, then insert
            entry.insert(0, ans)
            return
        elif value == 'x^3':
            ans = round(eval(ex)**3, 4)
        elif value == '+':
            entry.insert(END, '+')
            return
        elif value == '-':
            entry.insert(END, '-')
            return
        elif value == 'X':
            entry.insert(END, '*')
            return
        elif value == '÷':
            entry.insert(END, '/')
            return
        elif value == 'x^y':
            entry.insert(END, '**')
            return
        elif value == 'mod':
            entry.insert(END, '%')
            return
        elif value == '|x|':
            ans = round(abs(eval(ex)), 4)
        elif value == '∛x':
            ans = round((eval(ex))**(1/3), 4)
        elif value == '2^x':
            ans = round(2**(eval(ex)), 4)
        elif value == '10^x':
            ans = round(10**(eval(ex)), 4)
        elif value == '+/-':
            ans = -(eval(ex))
        elif value == 'rad':
            return
        elif value == '=':
            ans = round(eval(ex), 4)
        else:
            entry.insert(END, value)
            return
    
    except (SyntaxError, ValueError, ZeroDivisionError, OverflowError):  # Added more error types
        # Show error message instead of just passing
        entry.delete(0, END)
        entry.insert(0, "Error")
        return
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
        return
    
    # History management
    if c == 9:
        c = 1
        for i in range(1, 9):
            hisl = Label(root, text='                                            ', 
                        font=('times', 20, 'bold italic'), fg='white', bg='#122224')
            hisl.grid(row=i, column=8, pady=15, padx=60)
        
    entry.delete(0, END)
    entry.insert(0, ans)
    hisl = Label(root, text='', font=('times', 20, 'bold italic'), fg='white', bg='#122224')
    hisl.grid(row=c, column=8, pady=15, padx=60)
    
    if value == 'AC':
        pass
    elif value == 'deg':
        pass
    elif value in ['e^x', '2^x', '1/x']:
        c += 1
        hisl.config(text=value[0:2] + str(eval(entry.get().replace(str(ans), ex))) + '=' + str(ans))
    elif value == '10^x':
        c += 1
        hisl.config(text=value[0:3] + str(eval(entry.get().replace(str(ans), ex))) + '=' + str(ans))
    elif value in ['sin', 'cos', 'tan', 'log', 'ln']:  # Added 'ln' here
        c += 1
        original_ex = ex.replace('°', '') if ex.endswith('°') else ex
        hisl.config(text=value + '(' + original_ex + ')=' + str(ans))
    elif value in ['x²', 'n!']:
        c += 1
        hisl.config(text=ex + value[1] + '=' + str(ans))
    elif value in ['√x', '∛x']:    
        c += 1  
        hisl.config(text=value[0] + '(' + ex + ')=' + str(ans))
    elif value == 'x^3':
        c += 1
        hisl.config(text=ex + value[1::] + '=' + str(ans))
    elif value == '|x|': 
        c += 1  
        hisl.config(text=value[0] + ex + value[-1] + '=' + str(ans))
    else: 
        c += 1     
        hisl.config(text=ex + '=' + str(ans))

# Create main window
root = Tk()
root.title("Scientific Calculator")
root.config(bg='#122222')
root.geometry('900x496+300+300')

# Entry field
entry = Entry(root, width=70, bd=10, bg='#a7bed3', font=('times', 16, 'bold italic'))
entry.grid(row=0, column=0, columnspan=6, padx=90)

# Button layout
button_list = ['x^3', 'π', '2π', 'AC', 'mod', '⌫', 'x²', '1/x', 'sin', 'cos', 'tan', 'e^x', '√x',
               '(', ')', 'n!', '∛x', '÷', 'x^y', '7', '8', '9', '2^x', 'X', '10^x', '4', '5', '6', 
               'rad', '-', 'log', '1', '2', '3', 'deg', '+', 'ln', '|x|', '0', '.', '+/-', '=']

rv, cv = 1, 0
for i in button_list:
    butt = Button(root, width=12, height=2, text=i, bg='#a7bed3', fg='white', 
                  font=('times', 18, 'bold italic'), activebackground='#c6e2e9',
                  command=lambda butt=i: click(butt))
    butt.grid(row=rv, column=cv)
    cv += 1
    if cv >= 6:
        rv += 1
        cv = 0

# History label
hist = Label(root, text='HISTORY', font=('times', 20, 'bold italic'), fg='white', bg='#122222')
hist.grid(row=0, column=8, pady=15, padx=100)

root.mainloop()