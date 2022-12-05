from threading import Thread
from time import time

n = int(input("Input size matrix: "))
p = [x for x in range(1, n + 1)]
q = [x for x in range(1, n + 1)]


def matrix_r(p_vector, q_vector):
    matrix_def = []
    for pi in p_vector:
        for qj in q_vector:
            matrix_def.append(1 / (1 + abs(qj - pi)))
    return matrix_def


start_time = time()
matrix1 = matrix_r(p, q)
matrix2 = matrix_r(p, q)
end_time = time()
print(f"Output time without thread: {end_time - start_time}s")

thread1 = Thread(target=matrix_r, args=(p, q,))
thread2 = Thread(target=matrix_r, args=(p, q,))

start_time = time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time = time()
print(f"Output time with thread: {end_time - start_time}s")
