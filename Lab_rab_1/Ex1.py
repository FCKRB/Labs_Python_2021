Year = int(input("Введите год на проверку:"))
if Year % 4 == 0 and (Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "- Високосный")
else:
    print(Year, "- Не високосный")