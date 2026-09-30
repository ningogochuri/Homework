# price = input("Enter item price: ")
# quantity = input("Enter quantity: ")

# try:
#     price = float(price)
#     quantity = int(quantity)
#     total = price * quantity
# except ValueError:
#     print("Error: Both price and quantity must be valid numbers!")
# else:
#     print(f"Total price: ${total}")


    

age = input("Enter your age: ")
try:
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("User must be at least 18 years old to register.")
except ValueError as e:
    print(e)
finally:
    print("Registration process completed")





# fruits = ["apple", "banana", "cherry", "orange"]
# index = input("Enter an index number: ")
# try:
#     index = int(index)
#     print(f"Selected fruit: {fruits[index]}")
# except ValueError:
#     print("Invalid input! Please enter a whole number.")
# except IndexError:
#     print(f"Index out of bounds! Choose an index between 0 and {len(fruits)-1}.")
# else:
#     print("Successfully retrieved item!")