from threading import Thread
from time import time
import os

name = os.getcwd()


def generate_files(count):
    if count < 3:
        raise ValueError

    for i in range(count):
        with open(f"in{i}.txt", "w") as f:
            f.write("ok")
    for i in range(count):
        with open(f"dir1/in{count}.txt", "w") as f:
            f.write("ok")
    with open(f"in{count+2}.txt", "w") as f:
        f.write("key")
    with open(f"in{count+1}.txt", "w") as f:
        f.write("ke")
    with open(f"in{count}.txt", "w") as f:
        f.write("key key")
    with open(f"dir1/in{count}.txt", "w") as f:
        f.write("key key")


def find_key(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(file, "r") as f:
                    if f.read().find("key") != -1:
                        print(root + "\\" + file)


generate_files(20)

t1 = time()
find_key(name)
find_key(name)
print("Output time without thread: ", time() - t1)

t2 = time()
x1 = Thread(target=find_key, args=(name,))
x1.start()
x2 = Thread(target=find_key, args=(name,))
x2.start()
x1.join()
x2.join()
print("Output time with thread: ", time() - t2)
