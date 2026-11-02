# import requests

# BASE_URL = 'https://crudcrud.com/api/bf564ce17b1c4b98a14481f2ecc61982/products'

# product_data = {
#     "name": "Laptop",
#     "price": 2500,
#     "in_stock": True
# }

# try:
#     response = requests.post(
#         BASE_URL,
#         json=product_data,
#         timeout=10
#     )

#     response.raise_for_status()

#     print(response.json())

# except requests.exceptions.HTTPError as e:
#     print("HTTP Error:", e)

# except requests.exceptions.ConnectTimeout:
#     print("Server took too long")




# import requests

# BASE_URL = 'https://crudcrud.com/api/bf564ce17b1c4b98a14481f2ecc61982/products'

# try:
#     response = requests.get(
#         BASE_URL,
#         timeout=10
#     )

#     response.raise_for_status()

#     products = response.json()

#     for product in products:
#         print(f"Name: {product['name']}")
#         print(f"Price: {product['price']}")
#         print(f"ID: {product['_id']}")
#         print("--------------------")

# except requests.exceptions.HTTPError as e:
#     print("HTTP Error:", e)

# except requests.exceptions.ConnectTimeout:
#     print("Server took too long")

# except requests.exceptions.ConnectionError:
#     print("Connection Error")



# import requests

# BASE_URL = 'https://crudcrud.com/api/bf564ce17b1c4b98a14481f2ecc61982/products'

# product_id = '6ae8db9432e95a03e89efd9b'

# try:
#     response = requests.get(
#         f"{BASE_URL}/{product_id}",
#         timeout=10
#     )

#     response.raise_for_status()

#     product = response.json()

#     print(f"Name: {product['name']}")
#     print(f"Price: {product['price']}")
#     print(f"In stock: {product['in_stock']}")
#     print(f"ID: {product['_id']}")

# except requests.exceptions.HTTPError as e:
#     print("HTTP Error:", e)

# except requests.exceptions.ConnectTimeout:
#     print("Server took too long")

# except requests.exceptions.ConnectionError:
#     print("Connection Error")



# import requests

# BASE_URL = 'https://crudcrud.com/api/bf564ce17b1c4b98a14481f2ecc61982/products'

# product_id = '6ae8db9432e95a03e89efd9b'

# updated_data = {
#     "name": "Gaming Laptop",
#     "price": 3200,
#     "in_stock": True
# }

# try:
#     response = requests.put(
#         f"{BASE_URL}/{product_id}",
#         json=updated_data,
#         timeout=10
#     )

#     response.raise_for_status()

#     print("Status Code:", response.status_code)

#     check_response = requests.get(
#         f"{BASE_URL}/{product_id}",
#         timeout=10
#     )

#     check_response.raise_for_status()

#     print("Updated Product:")
#     print(check_response.json())

# except requests.exceptions.HTTPError as e:
#     print("HTTP Error:", e)

# except requests.exceptions.ConnectTimeout:
#     print("Server took too long")

# except requests.exceptions.ConnectionError:
#     print("Connection Error")




import requests

BASE_URL = 'https://crudcrud.com/api/bf564ce17b1c4b98a14481f2ecc61982/products'

product_id = '6ae8db9432e95a03e89efd9b'

try:
    response = requests.delete(
        f"{BASE_URL}/{product_id}",
        timeout=10
    )

    response.raise_for_status()

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Product successfully deleted from server!")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.ConnectTimeout:
    print("Server took too long")

except requests.exceptions.ConnectionError:
    print("Connection Error")