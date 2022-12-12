class Dog:
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        self.status = "hungry"
    def feed(self, meal, mass):
        print(self.name, "has been fed")
        self.weight += mass
        self.status = "not hungry"

        pass

sharik = Dog("sharik", "bulldog", 10, 20)
bobik = Dog('Bobik', 'pudle', 7, 10)
sharik.feed('beef', 0.2)
print(sharik.weight)

sharik.feed('beer', 0.5)
print(sharik.status)

