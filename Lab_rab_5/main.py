from product import Product


def input_price():
    while True:
        try:
            value = float(input("Input price (>= 0): "))
            if value < 0:
                print("Price < 0")
                continue
            return value
        except ValueError:
            print("Incorrect input")


name = input("Input name of product: ")
price = input_price()
manufacture = input("Input name of manufacture: ")

product1 = Product(name, price, manufacture)
print(product1)

product1.increase_price_rub(100)
print(product1)

try:
    with open("product.txt", "r") as file:
        cat = file.readline().split()
except IOError:
    print("File not found or problems with opening, don't worry i can create new file")
    with open("product.txt", "w") as file:
        file.write("Apple 40.0 Garden\n")
    with open("product.txt", "r") as file:
        cat = file.readline().split()

name = cat[0]
try:
    price = float(cat[1])
    if price < 0:
        price = 100.0
except ValueError:
    print("Incorrect input")
    price = 100.0

assert price >= 0.0

manufacture = cat[2]

product2 = Product(name, price, manufacture)
print(product2)
