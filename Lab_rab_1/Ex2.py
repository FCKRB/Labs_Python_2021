N = int(input("Введите натуральное число:"))
i = 0
l2 =[]
l1 = [0, 1, 5, 6, 25, 76, 376, 625, 9376, 90625, 109376, 890625,
     2890625, 7109376, 12890625, 87109376, 212890625,787109376, 1787109376]

while N > l1[i]:
    l2.append(l1[i])
    i = i + 1
print("Все автоморфные числа, которые меньше введенного числа", l2)
