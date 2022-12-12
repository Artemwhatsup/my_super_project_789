import re

a = ':-);------)'

a = re.findall(r"[:;]\-*[\(\)]+|[:;]\-*[\[\]]+", a)

print(a)


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
sharik = Dog("sharik", "bulldog", 10)
bobil = Dog('Bobik', 'pudle', 7)

sharik.breed
print(sharik.breed)