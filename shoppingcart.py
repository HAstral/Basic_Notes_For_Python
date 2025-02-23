foods = []
prices = []
total = 0

while True:
    food = input("Enter food (or type q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----Your Cart-----")
for f in foods:
    print(f,end=" | ")

for p in prices:
    total += p

print(f"\nTotal: ${total:.2f}")

