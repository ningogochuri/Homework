# #1

# age = int(input("Enter your age: "))

# if age < 0:
#     print("Invalid age entered.")
# elif age < 5:
#     price = 0
# elif age <= 12:
#     price = 8
# elif age <= 64:
#     price = 15
# else:
#     price = 10

# if age >= 0:
#     print(f"Your ticket price is ${price}.")

#2

cart_total = float(input("Enter cart: "))
is_vip = input("Are you a VIP member? (True/False): ") == "True"
promo_code = input("Enter promo code: ") == "SAVE10"
is_guest = input("Are you a guest user? (True/False): ") == "True"

if (cart_total >= 50 or is_vip) and promo_code and not is_guest:
    print("You get Free Shipping.")
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print("10% discount was applied.")

elif cart_total >= 50 or is_vip:
    print("You get Free Shipping.")
    final_total = cart_total
    print("No discount was applied.")

elif promo_code and not is_guest:
    print("You pay for shipping.")
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print("10% discount was applied.")

else:
    print("You pay for shipping.")
    final_total = cart_total
    print("No discount was applied.")

print(f"Final total price: {final_total}")