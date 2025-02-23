import math

# print(math.pi)
# print(math.e)

radius=float(input('Enter the radius: '))
circumstance=2*math.pi*radius
print(f'The circumstance of the circle is {round(circumstance,2)}')

area=math.pi * pow(radius,2)
print(f'The area of the circle is : {round(area,2)}')