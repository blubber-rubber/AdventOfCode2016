# JOSEPHUS PROBLEM
# https://en.wikipedia.org/wiki/Josephus_problem
# https://oeis.org/A006257

import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

n_elves = int(lines[0])


class Elf:
    def __init__(self, index):
        self.index = index
        self.next = None
        self.prev = None


first_elf = Elf(1)
prev_elf = first_elf
for index in range(2, n_elves + 1):
    new_elf = Elf(index)
    prev_elf.next = new_elf
    new_elf.prev = prev_elf
    prev_elf = new_elf

prev_elf.next = first_elf
first_elf.prev = prev_elf

current_elf = first_elf
dead_elf = current_elf
for _ in range(n_elves // 2):
    dead_elf = dead_elf.next

# approach: two pointers opposite on the circle of each other

while n_elves > 1:

    # kill elf

    prev_elf = dead_elf.prev
    next_elf = dead_elf.next

    prev_elf.next = next_elf
    next_elf.prev = prev_elf

    dead_elf.prev = None
    dead_elf.next = None

    if n_elves % 2 == 0:
        dead_elf = prev_elf
    else:
        dead_elf = next_elf

    ########################

    n_elves -= 1

    current_elf = current_elf.next
    dead_elf = dead_elf.next

print(current_elf.index)
print(time.time() - start_time)
