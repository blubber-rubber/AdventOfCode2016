import time
from collections import Counter

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

score = 0
for line in lines:
    name, checksum = line.split('[')
    name, checksum = name.split('-'), checksum.rstrip(']')
    room_name, sector_id = name[:-1], int(name[-1])
    c = Counter(''.join(room_name))
    if checksum == ''.join(sorted(c, key=lambda x: (-c[x], x)))[:5]:
        score += sector_id
print(score)

print(time.time() - start_time)
