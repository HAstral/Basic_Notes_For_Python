def add_sprinkles(func):
    def wrapper(*args,**kwargs): #need this to pass the function only when the func has been called
        print("You add sprinkles ✨ ")
        func(*args,**kwargs)
    return wrapper

def add_funge(func):
    def wrapper(*args,**kwargs):
        print("You add funge 🍫 ")
        func(*args,**kwargs)
    return wrapper


@add_sprinkles
@add_funge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("strawberry")