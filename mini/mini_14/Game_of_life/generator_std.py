import random


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = [[0 for j in range(self.width)] for i in range(self.height)]

    def count_neighbors(self, x, y):
        k = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    k += self.field[(y + i) % self.height][(x + j) % self.width]
        return k

    def generate_field(self):
        self.field = [[random.randint(0, 1) for j in range(self.width)] for i in range(self.height)]

    def print_field(self):
        for i in range(self.height):
            print(*self.field[i])

    def next_iteration(self):
        f_buf = [[0 for j in range(self.width)] for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                k = self.count_neighbors(j, i)

                if k >= 4 or k <= 1:
                    f_buf[i][j] = 0
                elif k == 2:
                    f_buf[i][j] = self.field[i][j]
                elif k == 3:
                    f_buf[i][j] = 1

        self.field = [[f_buf[i][j] for j in range(self.width)] for i in range(self.height)]