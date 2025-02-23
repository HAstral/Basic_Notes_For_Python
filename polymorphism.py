#inheritence
from abc import abstractmethod


class Shape():
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side **2


class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        return self.base * self.height *0.5

class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping=topping
        super().__init__(radius)


shapes=[Circle(5),Square(6),Triangle(7,8),Pizza('pepperoni',10)]

for s in shapes:
    print(f'{s.area()} cm²')