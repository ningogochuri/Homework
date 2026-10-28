
# class MovieTicket:
#     cinema_name = "Rustaveli Cinema"
#     total_tickets_sold = 0

#     def __init__(self, movie_title, seat_number, price):
#         self.movie_title = movie_title
#         self.seat_number = seat_number
#         self.price = price

#         MovieTicket.total_tickets_sold += 1


# ticket_1 = MovieTicket("Avatar", 10, 15)
# ticket_2 = MovieTicket("Titanic", 5, 20)
# ticket_3 = MovieTicket("Inception", 12, 18)

# print(ticket_1.cinema_name)
# print(ticket_1.movie_title)
# print(ticket_1.seat_number)
# print(ticket_1.price)

# print("=" * 40)

# print(ticket_2.cinema_name)
# print(ticket_2.movie_title)
# print(ticket_2.seat_number)
# print(ticket_2.price)

# print("=" * 40)

# print(ticket_3.cinema_name)
# print(ticket_3.movie_title)
# print(ticket_3.seat_number)
# print(ticket_3.price)

# print("=" * 40)

# print(f"Total tickets sold: {MovieTicket.total_tickets_sold}")





# class User:
#     status = "Active"

#     def __init__(self, username, email, age):
#         self.username = username
#         self.email = email
#         self.age = age

#     def get_info(self):
#         print("=" * 40)
#         print(f"Username: {self.username}")
#         print(f"Email: {self.email}")
#         print(f"Age: {self.age}")
#         print(f"Status: {self.status}")


# user_1 = User("john123", "john@gmail.com", 25)
# user_2 = User("anna456", "anna@gmail.com", 30)

# user_1.get_info()
# user_2.get_info()

# print("=" * 40)
# print(user_1.status)
# print(user_2.status)





class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        self.stock -= quantity
        print(f"Sold {quantity} {self.name}, remaining: {self.stock}")


product_1 = Product("laptops", 1500, 10)

print(product_1.shop_name)
print(product_1.name)
print(product_1.price)
print(product_1.stock)

product_1.sell(2)

print(product_1.stock)
