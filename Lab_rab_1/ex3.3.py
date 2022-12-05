l = list(map(int, input("Введите последовательность:").split()))
i = 0
fib1 = 0
fib2 = 1

isFindStart = False

while True:
    fib1, fib2 = fib2, (fib1 + fib2)
    if not isFindStart:
        if fib2 > l[0]:
            print(l, "- No")
            break
        elif fib2 == l[0]:
            isFindStart = True
            i += 1
            if i == len(l):
                print(l, "- Yes")
                break
    else:
        if fib2 == l[i]:
            i += 1
            if i == len(l):
                print(l, "- Yes")
                break
        else:
            print(l, "- No")
            break