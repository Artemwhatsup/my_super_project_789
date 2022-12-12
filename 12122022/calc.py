# calc.py
from exceptions import MyZeroDivisionError

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise MyZeroDivisionError(a)

