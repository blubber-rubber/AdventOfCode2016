import time
from functools import cache

start_time = time.time()

FAV_NUM = 1358

start = (1, 1)
end = (31,39)
r = 50
pad = []

def symbol_generator(x, y):
    if (x, y) in pad:
        return 'V'
    elif (x, y) in visited:
        return 'O'
    elif is_open(x, y):
        return '.'
    else:
        return '#'


@cache
def is_open(x, y):
    return sum([int(x) for x in str(bin(x * x + 3 * x + 2 * x * y + y + y * y + FAV_NUM))[2:]]) % 2 == 0


@cache
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] + p2[0])


visited = {start: 0}
positions = [start]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

chain = {start: None}

while end not in visited:
    positions.sort(key=lambda x: visited[x] + manhattan_distance(x, end))
    current_pos = positions.pop(0)
    cx, cy = current_pos

    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if nx >= 0 and ny >= 0 and (nx, ny) not in visited and is_open(nx, ny):
            visited[(nx, ny)] = visited[current_pos] + 1
            chain[(nx, ny)] = current_pos
            positions.append((nx, ny))


pos = end

while pos is not None:
    pad.append(pos)
    pos = chain[pos]

pad.reverse()




print('\n'.join([''.join(symbol_generator(x, y) for x in range(r)) for y in range(r)]))

print(pad)
print(visited[end])
print(time.time() - start_time)
