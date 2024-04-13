def add_product(products_list):
    name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    quantity = int(input("Введіть кількість товару: "))
    products_list.insert(0, (name, price, quantity))


def main():
    products = []

    add_product(products)
    add_product(products)

    print("Список товарів у магазині:")
    for product in products:
        print(f"Назва: {product[0]}, Ціна: {product[1]}, Кількість: {product[2]}")


if __name__ == "__main__":
    main()
