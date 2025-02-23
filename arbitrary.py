# def add(a,b):
#     return a+b

# print(add(1,2))

def add(*args):
    # print(type(args))
    total=0
    for arg in args:
        total += arg
    return total

# print(add(1,2,3,4,5,6,7,8,9,10))

def display_name(*args): #args is a tuple
    for arg in args:
        print(arg, end=" ")


# display_name("John","Doe")

def print_address(**kwargs): #kwargs is a dictionary
    for key,value in kwargs.items():
        # print(value,end=" - ")
        print(f"{key}: {value}")

print_address(name="John Doe", street="123 Main St", city="Anytown", state="AS", zip="12345")