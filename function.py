# def divide_remain(fnum,snum):
#     """Calculate the quotient and remainder"""
#     return fnum//snum, fnum%snum

# first, second=divide_remain(10,3)
# print('The quotient ; '+ str(first))
# print('The remainder : '+str(second))
def happy_birthday(name,age):
    print(f"Happy Birthday to {name},you are {age}!")
    print(f"Nobody Likes {name}!")
    print(f"{name} looks like a monkey!")
    print("Go Back To The Zoo!")
    print()

# happy_birthday("Mira",23)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due :{due_date}")
    print()

# display_invoice("BroHlyan",490,"31/03/2021")

def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

# print(add(1,2))

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

full_name=create_name("john","doe")

print(full_name)