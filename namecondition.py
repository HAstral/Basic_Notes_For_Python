name=input("Enter your name :")

# # res=name.len()
# # res=name.find(" ")
# # res=name.rfind("a")
# # name=name.capitalize()
# # name=name.upper() lower()
# res=name.isalpha() shows false when it contains space & non-alphabets
#count("a") will count all the a
#replace("a","b") will replace all a to b
if len(name) >12:
    print(f"Your name cannot longer than 12.")
elif not name.find(" ")==-1:
    print(f"No spaces are allowed")
elif not name.isalpha():
    print(f"No num allowed")
else:
    print(f"Name is verified.")