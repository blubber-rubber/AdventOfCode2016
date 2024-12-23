import time
import numpy as np

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

pos = (1, 1)

keypad = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])


def check_valid(pos):
    return 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2


def update(pos, direction):
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if check_valid(new_pos):
        pos = new_pos
    return pos


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

keys = []
for line in lines:
    for char in line:
        pos = update(pos, directions[char])
    keys.append(keypad[tuple(pos)])

print(''.join(str(i) for i in keys))
print(time.time() - start_time)
