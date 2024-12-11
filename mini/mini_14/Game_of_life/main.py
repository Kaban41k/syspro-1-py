import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import generator_std as gen_std
import generator_np as gen_np

WIDTH, HEIGHT = 128, 128

field_1 = gen_std.Field(WIDTH, HEIGHT)
field_1.generate_field()

field_2 = gen_np.Field(WIDTH, HEIGHT)
field_2.field = np.array(field_1.field)

figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


def next_iteration(frame):
    field_1.next_iteration()
    field_2.next_iteration()

    ax1.clear()
    ax2.clear()

    ax1.imshow(field_1.field, cmap='binary')
    ax2.imshow(field_2.field, cmap='binary')

    ax1.axis('off')
    ax2.axis('off')


def main():
    ax1.imshow(field_1.field, cmap='binary')
    ax2.imshow(field_2.field, cmap='binary')

    ax1.axis('off')
    ax2.axis('off')

    animation = FuncAnimation(figure, next_iteration, interval=20, cache_frame_data=False)

    plt.show()


if __name__ == "__main__":
    main()
