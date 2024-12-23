import time
import numpy as np
from itertools import product

start_time = time.time()

WIDTH = 50
HEIGHT = 6


def rect(A, B, screen):
    for a, b in product(range(A), range(B)):
        screen[b][a] = '█'


def rotate_col(x, d, screen):
    col = [screen[h][x] for h in range(HEIGHT)]
    col = col[-d:] + col[:-d]

    for h in range(HEIGHT):
        screen[h][x] = col[h]


def rotate_row(y, d, screen):
    row = [screen[y][w] for w in range(WIDTH)]
    row = row[-d:] + row[:-d]

    for w in range(WIDTH):
        screen[y][w] = row[w]


with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

for line in lines:

    if line.startswith('rect'):
        a, b = [int(x) for x in line.split(' ')[1].split('x')]
        rect(a, b, screen)
    elif line.startswith('rotate column'):
        x, d = [int(x) for x in line.split('=')[1].split(' by ')]
        rotate_col(x, d, screen)
    elif line.startswith('rotate row'):
        y, d = [int(x) for x in line.split('=')[1].split(' by ')]
        rotate_row(y, d, screen)

print('\n'.join([''.join(row) for row in screen]))

print(time.time() - start_time)
