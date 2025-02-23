temp =int(input("Enter the temperature: "))
is_raining = True

# if temp<0 or temp>50 or is_raining:
if temp > 50 and  is_raining:
    print("You cannot play outside.")
else: 
    print("You can go play outside.")