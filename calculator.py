import tkinter
from tkinter import *
from tkinter import ttk

"""
    Python Calculator
    By: Austin Paolello

    A simple calculator program. Can add, subtract, multiply, divide, modulo, and exponent
"""
display = "0"
num1 = 0
num2 = 0
operator = "null"
result = 0.0
currentNum = "num1"


def add():
    """
    A simple function to calculate the sum of two numbers
    :return:
    """
    global num1, num2, result
    result = num1 + num2


def subtract():
    """
    A simple function to calculate the difference of two numbers
    :return:
    """
    global num1, num2, result
    result = num1 - num2


def multiply():
    """
    A simple function to calculate the product of two numbers
    :return:
    """
    global num1, num2, result
    result = num1 * num2


def divide():
    """
    A simple function to calculate the quotient of two numbers
    :return:
    """
    global result, num1, num2
    while True:
        try:
            result = num1 / num2
            break
        except ZeroDivisionError:
            print("Can't divide by zero")
    if result.is_integer():
        result = int(result)


def modulo():
    """
    A simple function to calculate the remainder of two numbers
    :return:
    """
    global result, num1, num2
    result = num1 % num2


def exponent():
    """
    A simple function to calculate the exponent of two numbers
    :return:
    """
    global num1, num2, result
    result = num1
    if num2 == 0:
        return 1
    else:
        for i in range(int(num2) - 1):
            result *= num1


def clear_screen():
    """
    Clears the screen and sets all values to zero
    :return:
    """
    global display, num1, num2, result, operator
    display = "0"
    num1 = 0
    num2 = 0
    result = 0.0
    operator = "null"
    answer.config(text=display)


def update_screen():
    """
    Displays the result of calculations on the screen
    :return:
    """
    global display, result
    # To make sure thqat if we have 2.0 that it shows as 2 but if we have 2.5 it shows as 2.5
    if isinstance(result, float):
        if result.is_integer():
            result = int(result)
    display = str(result)
    answer.config(text=display)


def add_num_1():
    """
    Either displays just a 1 or adds a 1 to the number (like making 21 from 2)
    :return:
    """
    global display, operator
    if display == "0":
        display = "1"
    else:
        display += "1"
    answer.config(text=display)


def add_num_2():
    """
    Either displays just a 2 or adds a 2 to the number (like making 22 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "2"
    else:
        display += "2"
    answer.config(text=display)


def add_num_3():
    """
    Either displays just a 3 or adds a 3 to the number (like making 23 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "3"
    else:
        display += "3"
    answer.config(text=display)


def add_num_4():
    """
    Either displays just a 4 or adds a 4 to the number (like making 24 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "4"
    else:
        display += "4"
    answer.config(text=display)


def add_num_5():
    """
    Either displays just a 5 or adds a 5 to the number (like making 25 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "5"
    else:
        display += "5"
    answer.config(text=display)


def add_num_6():
    """
    Either displays just a 6 or adds a 6 to the number (like making 26 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "6"
    else:
        display += "6"
    answer.config(text=display)


def add_num_7():
    """
    Either displays just a 7 or adds a 7 to the number (like making 27 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "7"
    else:
        display += "7"
    answer.config(text=display)


def add_num_8():
    """
    Either displays just an 8 or adds an 8 to the number (like making 28 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "8"
    else:
        display += "8"
    answer.config(text=display)


def add_num_9():
    """
    Either displays just a 9 or adds a 9 to the number (like making 29 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "9"
    else:
        display += "9"
    answer.config(text=display)


def add_num_0():
    """
    Either displays just a 0 or adds a 0 to the number (like making 20 from 2)
    :return:
    """
    global display
    if display == "0":
        display = "0"
    else:
        display += "0"
    answer.config(text=display)


def set_op_add():
    """
    Sets the operator variable to add. Useful for calculate function
    :return:
    """
    global operator
    operator = "add"
    set_num()


def set_op_subtract():
    """
    Sets the operator variable to subtract. Useful for calculate function
    :return:
    """
    global operator
    operator = "subtract"
    set_num()


def set_op_multiply():
    """
    Sets the operator variable to multiply. Useful for calculate function
    :return:
    """
    global operator
    operator = "multiply"
    set_num()


def set_op_divide():
    """
    Sets the operator variable to divide. Useful for calculate function
    :return:
    """
    global operator
    operator = "divide"
    set_num()


def set_op_modulo():
    """
    Sets the operator variable to modulo. Useful for calculate function
    :return:
    """
    global operator
    operator = "modulo"
    set_num()


def set_op_exponent():
    """
    Sets the operator variable to exponent. Useful for calculate function
    :return:
    """
    global operator
    operator = "exponent"
    set_num()


def set_num():
    """
    Decide whether to take the number currently on our screen and store it in num1 or num2
    :return:
    """
    global currentNum, num1, num2, display
    if currentNum == "num1":
        num1 = float(display)
        currentNum = "num2"
        if num1.is_integer():
            answer.config(text=str(int(num1)))
        else:
            answer.config(text=str(num1))
        display = "0"
    else:
        num2 = float(display)
        currentNum = "num1"
        if num2.is_integer():
            answer.config(text=str(int(num2)))
        else:
            answer.config(text=str(num2))
        display = "0"


def calculate():
    """
    The main bridge between pressing equals (after setting up num1 and num2) that chooses one of our existing
    arithmetic functions and performs the operation. After it updates what our screen says, so we can see the answer
    :return:
    """
    global operator, display
    set_num()
    if operator != "null":
        if operator == "add":
            add()
        elif operator == "subtract":
            subtract()
        elif operator == "multiply":
            multiply()
        elif operator == "divide":
            divide()
        elif operator == "modulo":
            modulo()
        elif operator == "exponent":
            exponent()
        update_screen()


calc = Tk()
calc.geometry("400x250")
calc_frame = tkinter.Frame(calc, border=3, relief=tkinter.GROOVE)
calc_frame.grid()
answer = ttk.Label(calc_frame, text=display, justify=RIGHT, anchor="e")
answer.grid(row=0, column=0, columnspan=4, rowspan=4, sticky=tkinter.E)
ttk.Button(calc_frame, text="C", command=clear_screen).grid(row=4, column=0)
ttk.Button(calc_frame, text="+/-").grid(row=4, column=1)
ttk.Button(calc_frame, text="%", command=set_op_modulo).grid(row=4, column=2)
ttk.Button(calc_frame, text="/", command=set_op_divide).grid(row=4, column=3)
ttk.Button(calc_frame, text="7", command=add_num_7).grid(row=5, column=0)
ttk.Button(calc_frame, text="8", command=add_num_8).grid(row=5, column=1)
ttk.Button(calc_frame, text="9", command=add_num_9).grid(row=5, column=2)
ttk.Button(calc_frame, text="x", command=set_op_multiply).grid(row=5, column=3)
ttk.Button(calc_frame, text="4", command=add_num_4).grid(row=6, column=0)
ttk.Button(calc_frame, text="5", command=add_num_5).grid(row=6, column=1)
ttk.Button(calc_frame, text="6", command=add_num_6).grid(row=6, column=2)
ttk.Button(calc_frame, text="-", command=set_op_subtract).grid(row=6, column=3)
ttk.Button(calc_frame, text="1", command=add_num_1).grid(row=7, column=0)
ttk.Button(calc_frame, text="2", command=add_num_2).grid(row=7, column=1)
ttk.Button(calc_frame, text="3", command=add_num_3).grid(row=7, column=2)
ttk.Button(calc_frame, text="+", command=set_op_add).grid(row=7, column=3)
ttk.Button(calc_frame, text="0", command=add_num_0).grid(row=8, column=0)
ttk.Button(calc_frame, text=".").grid(row=8, column=1)
ttk.Button(calc_frame, text="exp", command=set_op_exponent).grid(row=8, column=2)
ttk.Button(calc_frame, text="=", command=calculate).grid(row=8, column=3)
calc.mainloop()
