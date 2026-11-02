# from dataclasses import dataclass,asdict

# import json
# @dataclass
# class Product:
#     name: str
#     price: float
#     in_stock: bool


# product1 = Product("iPhone 16", 2500, True)
# product2 = Product("MacBook Air", 3500, True)
# product3 = Product("AirPods", 700, False)


# # print(product1)
# # print(product2)
# # print(product3)


# products = [product1, product2, product3]

# products_dict = [asdict(product) for product in products]

# json_data = json.dumps(products_dict, indent=4)

# print(json_data)



from dataclasses import dataclass
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


json_data = '{"name": "Laptop", "price": 2500, "in_stock": true}'

data = json.loads(json_data)

p = Product(**data)

print(type(p))
print(p)

print(p.name)
print(p.price)
print(p.in_stock)