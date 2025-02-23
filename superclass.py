class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm²")

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of { self.width * self.width} cm²")


class Triangle(Shape):
     def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height
     def describe(self):
        super().describe()
        print(f"It is a triangle with an area of { self.width * self.height/2} cm²")



circle=Circle("red",True,5)
square=Square("blue",False,10)
triangle=Triangle("black",True,7,8)
# print(triangle.color)
# print(f"{triangle.width}cm")
triangle.describe() #7:17:04