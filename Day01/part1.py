import time
import numpy as np

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

directions = [np.array((int(np.cos(np.pi / 2 - i * np.pi / 2)), int(np.sin(np.pi / 2 - i * np.pi / 2)))) for i in
              range(4)]

d_index = 0
instructions = lines[0].split(', ')
pos = np.array([0, 0])

for instr in instructions:
    rotation, n = instr[0], int(instr[1:])
    if rotation == "R":
        d_index = (d_index + 1) % 4
    else:
        d_index = (d_index - 1) % 4

    pos += n * directions[d_index]

print(pos.sum())
print(time.time() - start_time)
