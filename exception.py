try:
    num = int(input("Enter a number:"))
    print(1/num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You have to enter a number!")
except Exception:
    print("Something went wrong!")
finally:
    print("Cleaning up here!")