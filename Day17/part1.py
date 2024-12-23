import time
import hashlib

start_time = time.time()

password = 'gdjjyniy'

current_positions = [((0, 0), '')]

searching = True

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
dir_names = 'UDLR'

while searching:
    pos, p = current_positions.pop(0)
    doors = hashlib.md5((password + p).encode()).hexdigest()[:4]

    cx, cy = pos
    for i in range(4):
        if doors[i] in 'bcdef':
            dx, dy = dirs[i]

            px = cx + dx
            py = cy + dy

            if 0 <= px < 4 and 0 <= py < 4:
                dn = dir_names[i]
                current_positions.append(((px, py), p + dn))

            if px == 3 and py == 3:
                searching = False
                break

print(current_positions[-1][1])
print(time.time() - start_time)
