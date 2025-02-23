weight=float(input("Enter your weight:"));
unit=input("Enter kilogram or pounds(Kgs or Lbs):")

if unit == "Kgs":
    weight=weight * 2.205
    unit = "Lbs"
elif unit == "Lbs":
    weight = weight/2.205
    unit = "Kgs"
else :
    print(f"The unit is invalid")

print (f"Your weight is {round(weight,2)} {unit}")