import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

nodes = []
for line in lines:
    m = re.match('/dev/grid/node-x([0-9]+)-y([0-9]+)[^0-9]*([0-9]+)T[^0-9]*([0-9]+)T[^0-9]*([0-9]+)*T', line)
    if m is not None:
        x, y, s, u, a = (int(x) for x in m.groups())

        nodes.append((x, y, u, a))

nodes.sort(key=lambda x: -x[-1])

index = 0
available_pairs = 0


for node in sorted(nodes, key=lambda x: -x[2]):
    if node[2] != 0:
        while index < len(nodes) and nodes[index][-1] > node[2]:
            index += 1
        available_pairs += index
        if node[3] > node[2]:
            available_pairs -= 1

print(available_pairs)
print(time.time() - start_time)
