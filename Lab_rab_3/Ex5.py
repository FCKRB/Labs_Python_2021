def num22(x):
    for i in range(len(x) - 1):
        if x[i + 1] < x[i]:
            return False
        if i == len(x) - 2:
            return True


print(num22([1, 2, 2, 3, 6, 12, 13]))