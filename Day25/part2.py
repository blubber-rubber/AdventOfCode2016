import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

"""
Today's solution was found by analyzing the input.txt file


Using the knowledge from part 1 we can speed our solution up further
"""

b = 0
d = 1

while b < 2550:
    b, d = 2 * b + d, 1 - d

print(b - 2550)

print(time.time() - start_time)
