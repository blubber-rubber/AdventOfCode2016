import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

score = 0
for line in lines:
    sides = sorted(int(i) for i in line.split(' ') if i != '')
    if sum(sides[:2]) > sides[2]:
        score += 1
print(score)
print(time.time() - start_time)
