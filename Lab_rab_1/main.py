N = int(input("Введите число:"))
num = 10
l = 0


def is_magic_number(x):
    return sum([int(i) for i in str(x)]) == 10


for a in range(N):
    if num % 9 == 1:
        num += 9
        l += 1
    while not is_magic_number(num):
        num += 9

if l == N:
    print(num)
