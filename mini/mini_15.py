import numpy as np
from numpy.linalg import matrix_power
from threading import Thread
from threading import Lock
import datetime

queue = []
the_end = False

CON_N = 100
TASKS_N = 200000


def producer():
    lock = Lock()
    size = 10
    value = 10
    times = 10

    for i in range(TASKS_N):
        lock.acquire()
        queue.append((size, value, times))
        lock.release()

    global the_end
    the_end = True


def consumer():
    lock = Lock()

    while len(queue) != 0 or not the_end:
        if len(queue) == 0:
            continue

        lock.acquire()
        size = queue[-1][0]
        value = queue[-1][1]
        times = queue[-1][2]
        queue.pop(-1)
        lock.release()

        a = np.zeros((size, size))

        for i in range(size):
            for j in range(size):
                a[i, j] = value ^ (i + j)

        matrix_power(a, times)
        result = np.sum(a)


start = datetime.datetime.now()

pro_t = Thread(target=producer(), args=[])
pro_t.start()

con_ts = []

for i in range(CON_N):
    con_ts.append(Thread(target=consumer(), args=[]))
    con_ts[i].start()

pro_t.join()

for i in range(CON_N):
    con_ts[i].join()

finish = datetime.datetime.now()

print(finish - start)
