from tkinter import *

# Create GUI window
window = Tk()
window.title("Simple Calculator")

# Define and put input field
entry = Entry(window, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "addition":
       entry.insert(0, f_num + int(second_number))
    elif math == "subtraction":
       entry.insert(0, f_num - int(second_number))
    elif math == "multiplication":
       entry.insert(0, f_num * int(second_number))
    elif math == "division":
       entry.insert(0, f_num / int(second_number))
    
btn_width = 10
btn_height = 3

# Define buttons
button_1 = Button(window, text="1", width=btn_width, height=btn_height, command=lambda: button_click(1))
button_2 = Button(window, text="2", width=btn_width, height=btn_height, command=lambda: button_click(2))
button_3 = Button(window, text="3", width=btn_width, height=btn_height, command=lambda: button_click(3))
button_4 = Button(window, text="4", width=btn_width, height=btn_height, command=lambda: button_click(4))
button_5 = Button(window, text="5", width=btn_width, height=btn_height, command=lambda: button_click(5))
button_6 = Button(window, text="6", width=btn_width, height=btn_height, command=lambda: button_click(6))
button_7 = Button(window, text="7", width=btn_width, height=btn_height, command=lambda: button_click(7))
button_8 = Button(window, text="8", width=btn_width, height=btn_height, command=lambda: button_click(8))
button_9 = Button(window, text="9", width=btn_width, height=btn_height, command=lambda: button_click(9))
button_0 = Button(window, text="0", width=24, height=btn_height, command=lambda: button_click(0))
button_clear = Button(window, text="Clear", width=24, height=btn_height, command=button_clear)
button_add = Button(window, text="+", width=btn_width, height=btn_height, command=button_add)
button_subtract = Button(window, text="-", width=btn_width, height=btn_height, command=button_subtract)
button_multiply = Button(window, text="×", width=btn_width, height=btn_height, command=button_multiply)
button_divide = Button(window, text="÷", width=24, height=btn_height, command=button_divide)
button_equal = Button(window, text="=", width=24, height=btn_height, command=button_equal)

# Put buttons in the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=2, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)

# Make loop
window.mainloop()