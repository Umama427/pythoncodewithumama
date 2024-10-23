#Day 13: 5th oct 2024

#Shopping cart
shopping_cart=[]
while True:
    items = input("Enter item name(or 'done' to 'finish'):")
    if items.lower()== 'done':
        break
    price = float(input("ENter item price:"))
    shopping_cart.append(price)

total_cost = sum(shopping_cart)
print(f"Total cost :${total_cost:.2f}")