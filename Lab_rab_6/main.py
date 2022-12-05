from threading import Thread
import time


def sleeper(n, name):
    print('Hello I {}. Want to sleep.'.format(name), sep="")
    time.sleep(n)
    print('{} wake up'.format(name))


t = Thread(target=sleeper, name="Thread1", args=(1, "Thread1",))
x1 = time.time()
t.start()

x2 = time.time()

print(x2 - x1)
