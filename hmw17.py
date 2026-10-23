
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, value):
#         if value >= 0:
#             self.__salary = value
#         else:
#             print("Salary cannot be negative!")

#     @salary.deleter
#     def salary(self):
#         del self.__salary


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")


# manager_1 = Manager("Nin", 10000, "IT")

# print(manager_1.salary)

# manager_1.get_info()





# class Payment:
#     def process_payment(self, amount):
#         print("მუშავდება გადახდა...")


# class CreditCardPayment(Payment):
#     def process_payment(self, amount):
#         print(f"საბანკო ბარათით გადახდილია: {amount} ლარი")


# class PayPalPayment(Payment):
#     def process_payment(self, amount):
#         print(f"PayPal-ით გადახდილია: {amount} ლარი")


# payment_1 = CreditCardPayment()
# payment_2 = PayPalPayment()

# payment_1.process_payment(100)
# payment_2.process_payment(200)





class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        print(f"{self.brand} is on")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.brand} is off")


class SmartLight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print(f"Brightness: {self.brightness}%")


light_1 = SmartLight("Samsung", 20)

light_1.turn_on()

print(light_1.__is_on)