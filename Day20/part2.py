import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

bounds = [(2 ** 32, 2 ** 32)]

for line in lines:
    lb, ub = [int(x) for x in line.split('-')]
    bounds.append((lb, ub))


def count_ips(bounds):
    count = 0
    if not any([lb == 0 for lb, rb in bounds]):
        count += min(bounds, key=lambda x: x[0])[0]

    bounds.sort(key=lambda x: x[1])

    for lb, ub in bounds[:-1]:
        pos = ub + 1

        if not any(lb <= pos <= ub for lb, ub in bounds):
            slb = min([lb for lb, ub in bounds if lb > pos])
            count += slb - pos

    return count


print(count_ips(bounds))

print(time.time() - start_time)
