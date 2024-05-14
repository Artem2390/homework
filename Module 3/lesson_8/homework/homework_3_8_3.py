import pickle
import json

# Список товарів в інтернет-магазині
products = [
    {"id": 1, "name": "Футболка", "price": 20.0},
    {"id": 2, "name": "Джинси", "price": 50.0},
    {"id": 3, "name": "Кросівки", "price": 80.0}
]

# Серіалізація за допомогою pickle
with open('products.pickle', 'wb') as pickle_file:
    pickle.dump(products, pickle_file)

print("Список товарів був серіалізований за допомогою pickle.")

# Серіалізація у форматі JSON
json_data = json.dumps(products, indent=4)

with open('products.json', 'w') as json_file:
    json_file.write(json_data)

print("Список товарів був серіалізований у форматі JSON.")
