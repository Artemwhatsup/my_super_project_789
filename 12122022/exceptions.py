# exceptions.py
class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, number):
        super().__init__(f"{number} was division by zero")
        self.number = number
