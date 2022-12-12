# main.py
from calc import div

try:
    result = div(100, 0)
    print("Расчёт проведён успешно")
except Exception as e:
    print("Вот такая ошибка деления произошла", e)
except TypeError as e:
    print(dir(e))
    print("Вот такая ошибка обращения по ключу произошла:", e)
else:
    print(result)
finally:
    print("Выполнение расчёта закончено")


hello hello
hello
hello hello
hellohello hello
hello


