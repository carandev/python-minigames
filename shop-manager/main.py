import os
import time

products_with_stock = ["Banana", "Pineapple",
                       "Apple", "Lemon", "Rice", "Bread"]


def main():
    os.system("clear")
    products = read_file("products")
    option = ask_for_input()

    while option != "4":

        os.system("clear")
        if option == "1":
            add_product()
        elif option == "2":
            remove_product()
        elif option == "3":
            show_products()
        else:
            print("Invalid option")

        option = ask_for_input()

    write_file("products", read_file("products"))


def ask_for_input():
    os.system("clear")
    print("Please select an option:")
    print("1) Add a new product")
    print("2) Remove a product")
    print("3) Show all products")
    print("4) Exit")
    return input("Enter your choice: ")


def add_product():
    os.system("clear")
    products = read_file("products")
    print("Write one product in stock")

    for product in products_with_stock:
        if product in products:
            print(f"[X] {product}")
        else:
            print(f"[] {product}")

    product_name = input("Enter the product name: ").capitalize()

    if product_name in products_with_stock:
        if product_name in products:
            print("This product is already in the list")
            time.sleep(2)
            return
        else:
            products.append(product_name)
            write_file("products", products)
    else:
        print("This product is not in stock")
        time.sleep(2)


def remove_product():
    os.system("clear")
    products = read_file("products")

    for i in range(len(products)):
        print(f"{i + 1}) {products[i]}")

    product_index = int(input("Enter the product number: ")) - 1

    products.remove(products[product_index])
    write_file("products", products)


def show_products():
    os.system("clear")
    products = read_file("products")
    print("Products:")
    for product in products:
        print(product)

    input("Press enter to continue")


def write_file(file_name, products):
    file = open(f"{file_name}.txt", "w")
    file.write("\n".join(products))
    file.close()


def read_file(file_name):
    file = open(f"{file_name}.txt", "r")
    products = file.read().splitlines()
    file.close()
    return products


if __name__ == "__main__":
    main()
