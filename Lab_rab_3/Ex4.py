def num21(a, b):
    x = []
    for i in range(a, b + 1):
        dels = 0
        for j in range(1, i // 2):
            if i % j == 0:
                dels += 1
        x.append(dels)
    y = []
    for i in range(len(x)):
        if x[i] == 1:
            y.append(i + a)
    return tuple(y)


print(num21(5, 154))