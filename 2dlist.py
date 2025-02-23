# fruits=    ["apple","banana","cherry"]
# vegetables=["carrot","potato","onion"]
# meats=     ["beef","chicken","pork"]

# groceries=[fruits,vegetables,meats]
groceries=({"apple","banana","cherry"},{"carrot","potato","onion"},{"beef","chicken","pork"})
# print(groceries)
# print(groceries[0][2])
for collections in groceries:
    for item in collections:
        print(item,end=" | ")
    print()