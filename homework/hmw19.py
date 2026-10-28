def shopping_cart():
    cart = ["Apple", "Cheese", "Bread"]

    cart.append("Milk")
    print("Shopping cart:", cart)

    cart.pop()
    print("After removing the last product:", cart)

    return cart


print(shopping_cart())






# def unique_users():
#     usernames = ["Nia", "Nini", "Gio", "Nia", "Nika", "Gio", "Nika"]

#     unique_names = set(usernames)

#     print("Unique users:", unique_names)
#     print("Number of unique users:", len(unique_names))


# unique_users()




# def search_contact():
#     phonebook = {
#         "Giorgi": "512365456",
#         "Ana": "55339988",
#         "Nino": "77332288",
#         "Nika": "99331177"
#     }

#     name = input("Enter a name: ")

#     print(phonebook.get(name, "Not found"))


# search_contact()


# def search_contact():
#     phonebook = {
#         "Giorgi": "555123456",
#         "Ana": "12334557",
#         "Nino": "555112233",
#         "Nika": "5558863322"
#     }

#     name = input("Enter a name: ")

#     return f"{name} {phonebook.get(name, 'ვერ მოიძებნა')}"


# print(search_contact())