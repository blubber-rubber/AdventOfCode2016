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
prev_positions = set()

for instr in instructions:
    rotation, n = instr[0], int(instr[1:])
    if rotation == "R":
        d_index = (d_index + 1) % 4
    else:
        d_index = (d_index - 1) % 4
    for _ in range(n):
        prev_positions.add(tuple(pos))
        pos += directions[d_index]
        if tuple(pos) in prev_positions:
            break
    if tuple(pos) in prev_positions:
        break

print(pos.sum())
print(time.time() - start_time)
