class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking. Woof Woof !")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing. Meow Meow !")

class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking. Squeak Squeak !")

dog=Dog("Rex")
cat=Cat("Tom")
mouse=Mouse("Jerry")

# print(cat.sleep())
mouse.squeak()
dog.bark()
cat.meow() #7:00:00