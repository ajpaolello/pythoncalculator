import tkinter
from tkinter import *
from tkinter import ttk

"""
    Python Calculator
    By: Austin Paolello

    A simple calculator program. Can add, subtract, multiply, divide, and modulo
    Right now it is only able to accept two numbers as inputs, but I plan on fixing this
    Other plans include adding a GUI
"""
display = "0"
num1 = 0
num2 = 0
operator = "null"
result = 0
currentNum = "num1"


def add():
    """
    A simple function to calculate the sum of two numbers
    :param num1: a numeric value
    :param num2: another numeric value
    :return: sum of num1 and num2
    """
    num1 += num2
    return num1


def subtract():
    """
    A simple function to calculate the difference of two numbers
    :param num1: a numeric value
    :param num2: another numeric value
    :return: difference of num1 and num2
    """
    num1 -= num2
    return num1


def multiply():
    """
    A simple function to calculate the product of two numbers
    :param num1: a numeric value
    :param num2: another numeric value
    :return: product of num1 and num2
    """
    num1 *= num2
    return num1


def divide():
    """
    A simple function to calculate the quotient of two numbers
    :param num1: a numeric value
    :param num2: another numeric value
    :return: quotient of num1 and num2
    """
    while True:
        try:
            num1 /= num2
            break
        except ZeroDivisionError:
            print("Can't divide by zero")
            # Get a new num2 value
            while True:
                num2 = input("Please enter the second number: ")
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print("Please enter a number!!")
    if num1.is_integer():
        num1 = int(num1)
    return num1


def modulo():
    """
    A simple function to calculate the remainder of two numbers
    :param num1: a numeric value
    :param num2: another numeric value
    :return: remainder of num1 and num2
    """
    num1 %= num2
    return num1


def exponent():
    """
    A simple function to calculate the exponent of two numbers
    :param num1: a numeric value
    :param num2: another numeric value
    :return: exponent of num1 and num2
    """
    result = num1
    if num2 == 0:
        return 1
    else:
        for i in range(int(num2) - 1):
            result *= num1
        return result


def clear_screen():
    global display
    display = "0"
    answer.config(text=display)


def add_num_1():
    global display
    if display == "0":
        display = "1"
    else:
        display += "1"
    answer.config(text=display)


def add_num_2():
    global display
    if display == "0":
        display = "2"
    else:
        display += "2"
    answer.config(text=display)


def add_num_3():
    global display
    if display == "0":
        display = "3"
    else:
        display += "3"
    answer.config(text=display)


def add_num_4():
    global display
    if display == "0":
        display = "4"
    else:
        display += "4"
    answer.config(text=display)


def add_num_5():
    global display
    if display == "0":
        display = "5"
    else:
        display += "5"
    answer.config(text=display)


def add_num_6():
    global display
    if display == "0":
        display = "6"
    else:
        display += "6"
    answer.config(text=display)


def add_num_7():
    global display
    if display == "0":
        display = "7"
    else:
        display += "7"
    answer.config(text=display)


def add_num_8():
    global display
    if display == "0":
        display = "8"
    else:
        display += "8"
    answer.config(text=display)


def add_num_9():
    global display
    if display == "0":
        display = "9"
    else:
        display += "9"
    answer.config(text=display)


calc = Tk()
calc.geometry("300x158")
calc_frame = tkinter.Frame(calc, border=3, relief=tkinter.GROOVE)
calc_frame.grid()
operator = "null"
answer = ttk.Label(calc_frame, text=display, justify=RIGHT, anchor="e")
answer.grid(row=0, column=0, columnspan=4, rowspan=4, sticky=tkinter.E)
ttk.Button(calc_frame, text="C", command=clear_screen).grid(row=4, column=0)
ttk.Button(calc_frame, text="+/-").grid(row=4, column=1)
ttk.Button(calc_frame, text="exp").grid(row=4, column=2)
ttk.Button(calc_frame, text="/").grid(row=4, column=3)
ttk.Button(calc_frame, text="7", command=add_num_7).grid(row=5, column=0)
ttk.Button(calc_frame, text="8", command=add_num_8).grid(row=5, column=1)
ttk.Button(calc_frame, text="9", command=add_num_9).grid(row=5, column=2)
ttk.Button(calc_frame, text="x").grid(row=5, column=3)
ttk.Button(calc_frame, text="4", command=add_num_4).grid(row=6, column=0)
ttk.Button(calc_frame, text="5", command=add_num_5).grid(row=6, column=1)
ttk.Button(calc_frame, text="6", command=add_num_6).grid(row=6, column=2)
ttk.Button(calc_frame, text="-").grid(row=6, column=3)
ttk.Button(calc_frame, text="1", command=add_num_1).grid(row=7, column=0)
ttk.Button(calc_frame, text="2", command=add_num_2).grid(row=7, column=1)
ttk.Button(calc_frame, text="3", command=add_num_3).grid(row=7, column=2)
ttk.Button(calc_frame, text="+").grid(row=7, column=3)
ttk.Button(calc_frame, text="0").grid(row=8, column=0, columnspan=2, sticky=tkinter.W+tkinter.E)
ttk.Button(calc_frame, text=".").grid(row=8, column=2)
ttk.Button(calc_frame, text="=").grid(row=8, column=3)
calc.mainloop()


"""
def main():
    # Basic menu and instructions
    print("Welcome to the Python Calculator!")
    print("I can do addition, subtraction, multiplication, division, and modulo")
    print("At the moment I can only do two numbers, but that should change in the future")
    print("Please enter which operation you wish to do:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Division with whole numbers")
    print("6. Modulo")
    print("7. Exponent")
    print("8. Quit")
    print()
    choice = 0
    num1 = 0
    num2 = 0
    result = 0
    while choice < 1 or choice > 8:
        choice = int(input("Please enter your choice: "))
        if 7 >= choice >= 1:
            # Making sure user entered a number
            while True:
                num1 = input("Please enter the first number: ")
                try:
                    num1 = float(num1)
                    break
                except ValueError:
                    print("Please enter a number!!")
            # Checking the second number
            while True:
                num2 = input("Please enter the second number: ")
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print("Please enter a number!!")
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 6:
            result = modulo(num1, num2)
        elif choice == 7:
            result = exponent(num1, num2)
        elif choice == 8:
            break
        else:
            print("Please enter a valid choice!!")

        if 1 <= choice <= 7:
            # Print result and ask to do another calculation
            print("The result is: ", result)
            answer = input("Would you like to perform another calculation? (y/n): ")
            if answer == "y" or answer == "Y":
                choice = 0


# Runs main function
calculator()
"""