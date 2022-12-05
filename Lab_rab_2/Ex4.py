with open("input41.txt", "r") as f:
    d = f.readlines()
    d_set = set()
    for line in d:
        d_set.update([word.replace("\n", '') for word in line.split(' ')])

d1 = set(d)

with open("input42.txt", "r") as f:
    e = f.readlines()
    e_set = set()
    for line in e:
        e_set.update([word.replace("\n", '') for word in line.split(' ')])

e1 = set(e)

k = d_set.intersection(e_set)

open("Result.txt", "w").close()  # Create the file

with open("Result.txt", "a") as f:
    f.write(str(k))