from script1 import *
# print(__name__)
def fav_drink(drink):
    print(f"My favorite drink is {drink}")


def main():
    print("This is script2.py")
    fav_food("sushi")
    fav_drink("coffee")
    print("Goodbye, World!")

if __name__ == "__main__":
    main()