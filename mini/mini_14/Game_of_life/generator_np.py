import random
import numpy as np


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = np.zeros((width, height))

    def count_neighbors(self):
        n = np.zeros((self.width, self.height))

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    n += np.roll(np.roll(self.field, i, 0), j, 1)

        return n

    def generate_field(self):
        self.field = np.array([[random.randint(0, 1) for j in range(self.width)] for i in range(self.height)])

    def print_field(self):
        for i in range(self.height):
            print(*self.field[i])

    def next_iteration(self):
        f_buf = np.zeros((self.width, self.height))

        n = self.count_neighbors()

        for i in range(self.height):
            for j in range(self.width):
                if n[i, j] >= 4 or n[i, j] <= 1:
                    f_buf[i, j] = 0
                elif n[i, j] == 2:
                    f_buf[i, j] = self.field[i][j]
                elif n[i, j] == 3:
                    f_buf[i, j] = 1

        self.field = f_buf
