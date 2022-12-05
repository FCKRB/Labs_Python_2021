l = list(map(int, input("Введите последовательность:").split()))

l1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
i = 0
j = 0

for a in range(len(l1)):
    if l[i] != l1[j]:
        j = j + 1
        continue
    else:
        break

for i in range(len(l)):
    if l[i] == l1[j]:
        j = j + 1
        i = i + 1
        continue
    else:
        print(l, "- No")
        break

if i == len(l):
    print(l, "- Yes")