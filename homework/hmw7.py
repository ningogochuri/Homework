price = input("Enter item price: ")
quantity = input("Enter quantity: ")

try:
    price = float(price)
    quantity = int(quantity)
    total = price * quantity
except ValueError:
    print("Error: Both price and quantity must be valid numbers!")
else:
    print(f"Total price: ${total}")