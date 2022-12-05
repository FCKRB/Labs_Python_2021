from product import Product
from food import Food
from smartphone import Smartphone
from desert import Desert

name = input("Enter product name: ")
value = 0.0
while True:
    try:
        value = float(input("Input price in rubs: "))
        break
    except ValueError:
        print("Incorrect input")
        print("Try more")

manufacturer = input("Enter manufacturer: ")

product1 = Product(name, value, manufacturer)
print(product1)
product1.print_with_euros()

product1.increase_price_rub(24)
product1.print_with_euros()

food1 = Food("Apple", 20.0, "Yablonevaya alley", 90)
print(food1)

smartphone1 = Smartphone("Galaxy A70", 50000.0, "Samsung", 8192)
print(smartphone1)
smartphone1.increase_price_rub(10000)
print(smartphone1)

smartphone2 = Smartphone("Mi 28", 25000.0, "Xiao", 4096)
print(smartphone2)
smartphone2.increase_price_rub(10000)
print(smartphone2)

desert1 = Desert("Tiramisu", 400.0, "Vova", 100, 50)
print(desert1)
