# try:
#     birth_year = int(input("Enter your birth year: "))
#     age = 2026 - birth_year
#     print(f"Your age is {age}")

# except ValueError:
#     print("Please enter only digits!")

try:
    password = input("Enter your password: ")

    if len(password) < 6:
        raise ValueError("Password is too short!")

except ValueError as e:
    print(e)