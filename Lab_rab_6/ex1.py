from threading import Thread
from time import time, sleep


# with join
thread1 = Thread(target=sleep, args=(3,))
thread2 = Thread(target=sleep, args=(5,))

start_time = time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time = time()
print(f"Execution time: {end_time - start_time}s")

# without join
thread1 = Thread(target=sleep, args=(3,))
thread2 = Thread(target=sleep, args=(5,))

start_time = time()
thread1.start()
thread2.start()
end_time = time()
print(f"Execution time: {end_time - start_time}s")
