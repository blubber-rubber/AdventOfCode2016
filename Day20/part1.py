import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

bounds = []

for line in lines:
    lb, ub = [int(x) for x in line.split('-')]
    bounds.append((lb, ub))


def get_lowest_ip(bounds):
    if not any([lb == 0 for lb, rb in bounds]):
        return 0

    bounds.sort(key=lambda x: x[1])

    for lb, ub in bounds:
        pos = ub + 1

        if not any(lb <= pos <= ub for lb, ub in bounds):
            return pos


print(get_lowest_ip(bounds))

print(time.time() - start_time)
