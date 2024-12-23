import time
import re
from heapq import heappush, heappop
from collections import defaultdict
import math

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

nodes = []
for line in lines:
    m = re.match('/dev/grid/node-x([0-9]+)-y([0-9]+)[^0-9]*([0-9]+)T[^0-9]*([0-9]+)T[^0-9]*([0-9]+)*T', line)
    if m is not None:
        x, y, s, u, a = (int(x) for x in m.groups())

        nodes.append((x, y, u, a))

N_COLS = max(n[0] for n in nodes) + 1
N_ROWS = max(n[1] for n in nodes) + 1
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def heuristic(pos):
    return sum(pos)


smalles_space = min(sum(n[-2:]) for n in nodes)

walls = {(x, y) for x, y, u, a in nodes if u > smalles_space}

open_pos = [(x, y) for x, y, u, a in nodes if u == 0][0]
states = []
d_pos = (N_COLS - 1, 0)
heappush(states, (heuristic(d_pos), 0, d_pos, open_pos))
visited = defaultdict(lambda: math.inf)

while states[0][2] != (0, 0):
    h, steps, d_pos, open_pos = heappop(states)
    cox, coy = open_pos

    if steps <= visited[(d_pos, open_pos)]:
        for dx, dy in DIRS:
            nx, ny = cox + dx, coy + dy
            no_pos = (nx, ny)
            nd_pos = d_pos
            if no_pos == d_pos:
                nd_pos = open_pos
            if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and no_pos not in walls and steps + 1 < visited[(nd_pos, no_pos)]:
                visited[(nd_pos, no_pos)] = steps + 1
                heappush(states, (steps + 1 + heuristic(nd_pos), steps + 1, nd_pos, no_pos))

print(states[0][1])
print(time.time() - start_time)
