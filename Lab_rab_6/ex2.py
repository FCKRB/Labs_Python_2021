import threading
import time
from threading import Condition

cond = Condition()
stop = False


def consumer():
    global stop
    while True:
        with cond:
            cond.wait()
            if stop:
                return
            print("Consumer")


def producer():
    global stop
    for i in range(10):
        with cond:
            stop = i == 9
            cond.notify()
        time.sleep(0.5)


threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
