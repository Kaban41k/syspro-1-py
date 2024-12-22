from threading import Thread
from threading import Lock
import datetime

queue = []
the_end = False
lock = Lock()

TASKS_N = 100000


def matrix_power(a, iterations):
    length = len(a[0])
    b = a
    c = [[0 for i in range(length)] for j in range(length)]

    for iteration in range(iterations):
        for i in range(length):
            for j in range(length):
                for l in range(length):
                    c[i][j] += a[i][l] * b[l][j]

        for i in range(length):
            for j in range(length):
                a[i][j] = c[i][j]

        c = [[0 for i in range(length)] for j in range(length)]


def producer():
    size = 4
    value = 10
    times = 3

    for i in range(TASKS_N):
        lock.acquire()
        queue.append((size, value, times))
        lock.release()

    global the_end
    the_end = True


def consumer():
    global queue

    while len(queue) != 0 or not the_end:
        lock.acquire()
        if len(queue) == 0:
            lock.release()
            continue

        size = queue[len(queue) - 1][0]
        value = queue[len(queue) - 1][1]
        times = queue[len(queue) - 1][2]
        queue.pop(-1)
        lock.release()

        a = [[0 for i in range(size)] for j in range(size)]

        for i in range(size):
            for j in range(size):
                a[i][j] = value ^ (i + j)

        matrix_power(a, times)


for CON_N in range(1, 30):
    queue = []
    the_end = False
    
    pro_t = Thread(target=producer, args=[])
    pro_t.start()

    con_ts = []

    start = datetime.datetime.now()

    for i in range(CON_N):
        con_ts.append(Thread(target=consumer, args=()))
        con_ts[i].start()

    pro_t.join()

    for i in range(CON_N):
        con_ts[i].join()

    finish = datetime.datetime.now()

    print(CON_N, " " * (3 - len(str(CON_N))) + "Time:", str(finish - start)[(str(finish - start).rfind(":") + 1):])
