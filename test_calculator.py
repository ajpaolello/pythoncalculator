"""
    Test for Calculator.py
    By: Austin Paolello

    Need to comment out the main method in calculator.py for this to work
    Probably should fix that
"""
from calculator import add, subtract, multiply, divide, divide_whole, modulo, exponent

num1 = 3
num2 = 2


def test_add():
    assert add(num1, num2) == 5.0


def test_subtract():
    assert subtract(num1, num2) == 1.0


def test_multiply():
    assert multiply(num1, num2) == 6.0


def test_divide():
    assert divide(num1, num2) == 1.5


def test_whole_divide():
    assert divide_whole(num1, num2) == 1.0


def test_modulo():
    assert modulo(num1, num2) == 1.0


def test_exponent():
    assert exponent(num1, num2) == 9.0

