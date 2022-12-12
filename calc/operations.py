import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="history.py", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")


a = int(input("введите число "))
b = int(input("введите число "))
c = str(input("введите действие "))

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "**":
    print(a ** b)
else:
    print("что то не так")

