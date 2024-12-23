import time
from hashlib import md5
from collections import defaultdict
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

salt = lines[0]

threes: dict[int, set] = defaultdict(set)
fives: dict[int, set] = defaultdict(set)


def update_3and5(index, threes, fives):
    hash = md5(bytes(f'{salt}{index}', 'utf-8')).hexdigest()

    repeats = re.search(r'([a-f0-9])\1{2}', hash)
    if repeats:
        threes[index].add(repeats.groups()[0])

    for m in re.finditer(r'([a-f0-9])\1{4}', hash):
        fives[index].add(m.groups()[0])


for index in range(1000):
    update_3and5(index, threes, fives)

good_ones = []
index = 0
while len(good_ones) < 64:
    update_3and5(index + 1000, threes, fives)
    if threes[index].intersection(set.union(*[fives[s] for s in range(index + 1, index + 1001)])):
        good_ones.append(index)
    index += 1

print(good_ones[-1])
print(time.time() - start_time)
