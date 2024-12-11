import datetime

WIDTH, HEIGHT = 128, 128

ITERATIONS = 100

import Game_of_life.generator_std as gen

f = gen.Field(WIDTH, HEIGHT)
f.generate_field()

start = datetime.datetime.now()

for iteration in range(ITERATIONS):
    f.next_iteration()

finish = datetime.datetime.now()

print(finish - start)

del gen

import Game_of_life.generator_np as gen

f = gen.Field(WIDTH, HEIGHT)
f.generate_field()

start = datetime.datetime.now()

for iteration in range(ITERATIONS):
    f.next_iteration()

finish = datetime.datetime.now()

print(finish - start)
