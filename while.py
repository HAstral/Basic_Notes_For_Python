# name=input("Enter your name:")

# while name=="":
#     print("You didn't enter your name.")
#     name=input("Enter your name:")
# print(f"Hello {name}")

food=input("Enter the food you like(type Q to quit): ")
while not food=="Q":
    print(f"You like {food}")
    food=input("Enter the food you like(type Q to quit): ")
print("Goodbye")

