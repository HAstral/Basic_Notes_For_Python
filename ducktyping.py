#duck typing to achieve polymorphism

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("WOOF!!")

class Cat(Animal):
    def speak(self):
        print("MEOW!!")

class Car:
    alive=False
    def speak(self):
        print("HONK!!")

animals=[Dog(),Cat(),Car()]

for a in animals:
    a.speak()
    print(a.alive) #7:33:35