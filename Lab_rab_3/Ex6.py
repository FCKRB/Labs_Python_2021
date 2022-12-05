def num23(*args):
    t = set(args[0])
    args = map(set, args)
    for i in args:
        t.intersection_update(i)
    return t

print(num23((1, 23, 123, 12), (7, 12, 11, 123)))