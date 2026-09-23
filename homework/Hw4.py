#1

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")
elif age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age <= 64:
    price = 15
else:
    price = 10

if age >= 0:
    print(f"Your ticket price is ${price}.")

#2

cart_total = float(input("Enter cart: "))
is_vip = False
promo_code = input("Enter promo code: ") == "SAVE10"
is_guest = True

if cart_total >= 50 or is_vip:
    print("You get Free Shipping.")
else:
    print("You pay for shipping.")

if promo_code and not is_guest:
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print("10% discount was applied.")
else:
    final_total = cart_total
    print("No discount was applied.")

print("Final total price:", final_total)

#3
correct_pin = 4652
balance = 10000.0
requested_amount = 0.0

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    requested_amount = float(input("Enter withdrawal amount: "))

    if requested_amount <= balance:
        balance = balance - requested_amount
        print(f"Withdrawal successful! Remaining balance: ${balance}")
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")
