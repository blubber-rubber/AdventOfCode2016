import math
import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    grid = [line.rstrip('\n') for line in f.readlines()]

start_position = None
N_ROWS = len(grid)
N_COLS = len(grid[0])

specials = []
DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '0':
            start_position = (x, y)
        if c not in '.#':
            specials.append(c)

visited = defaultdict(lambda: math.inf)
visited[(start_position, (0,))] = 0
states = [(0, start_position, (0,))]

while states and len(states[0][2]) != len(specials):
    steps, pos, found_specials = states.pop(0)
    cx, cy = pos

    if steps <= visited[(pos, found_specials)]:

        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and grid[ny][nx] != '#':
                new_pos = (nx, ny)
                new_found = set(found_specials)
                if grid[ny][nx] != '.':
                    new_found.add(int(grid[ny][nx]))
                new_found = tuple(sorted(new_found))

                if steps + 1 < visited[(new_pos, new_found)]:
                    visited[(new_pos, new_found)] = steps + 1
                    states.append((steps + 1, new_pos, new_found))

print(states[0][0])
print(time.time() - start_time)
