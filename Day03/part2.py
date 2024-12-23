import time
import numpy as np

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

score = 0
for index in range(0, len(lines), 3):
    rows = np.array([[int(i) for i in lines[index].split(' ') if i != ''],
                     [int(i) for i in lines[index + 1].split(' ') if i != ''],
                     [int(i) for i in lines[index + 2].split(' ') if i != '']]).T
    for sides in rows:
        sides.sort()
        if sum(sides[:2]) > sides[2]:
            score += 1

print(score)
print(time.time() - start_time)
