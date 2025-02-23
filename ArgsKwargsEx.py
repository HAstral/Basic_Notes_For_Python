def shipping_address(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}" )
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_address("Dr.","Spangebob","Squarepants",
                 street="123 Main St",apt="Nyein Chan Rooftop", city="Anytown",
                   state="AS", zip="12345")