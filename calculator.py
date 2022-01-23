"""
    Python Calculator
    By: Austin Paolello

    A simple calculator program. Can add, subtract, multiply, divide, and modulo
    Right now it is only able to accept two numbers as inputs, but I plan on fixing this
    Other plans include adding a GUI
"""


def add(num1, num2):
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    difference = num1 - num2
    return difference


def multiply(num1, num2):
    product = num1 * num2
    return product


def divide(num1, num2):
    quotient = num1 / num2
    return quotient


def divide_whole(num1, num2):
    quotient = num1 // num2
    return quotient


def modulo(num1, num2):
    remainder = num1 % num2
    return remainder


def main():
    print("Welcome to the Python Calculator!")
    print("I can do addition, subtraction, multiplication, division, and modulo")
    print("At the moment I can only do two numbers, but that should change in the future")
    print("Please enter which operation you wish to do:")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Division with whole numbers")
    print("6. Modulo")
    print("7. Quit")
    print()
    choice = 0
    num1 = 0
    num2 = 0
    result = 0
    while choice < 1 or choice > 7:
        choice = int(input("Please enter your choice: "))
        if 7 >= choice >= 1:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = divide_whole(num1, num2)
        elif choice == 6:
            result = modulo(num1, num2)
        elif choice == 7:
            break
        else:
            print("Please enter a valid choice!!")

    if 1 <= choice <= 7:
        print("The result is: ", result)


main()
