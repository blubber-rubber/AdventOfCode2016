# JOSEPHUS PROBLEM
# https://en.wikipedia.org/wiki/Josephus_problem
# https://oeis.org/A006257

import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

desired = int(lines[0])


def josephus(n, sols):
    if n % 2 == 0:
        sols[n] = 2 * sols[n // 2] - 1

    else:
        sols[n] = 2 * sols[n // 2] + 1


solutions = {1: 1, 2: 1}

for n in range(3, desired + 1):
    josephus(n, solutions)

print(solutions[desired])
print(time.time() - start_time)
