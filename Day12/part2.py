import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

REGISTERS = {'a': 0, 'b': 0, 'c': 1, 'd': 0}


def cpy(x, y, registers=REGISTERS):
    if x in registers:
        registers[y] = registers[x]
    else:
        registers[y] = int(x)


def inc(x, registers=REGISTERS):
    registers[x] += 1


def dec(x, registers=REGISTERS):
    registers[x] -= 1


def jnz(x, y, registers=REGISTERS):
    if x in registers:
        x = registers[x]

    if y in registers:
        y = registers[y]

    if int(x) != 0:
        return int(y)


pointer = 0

functions = {'cpy': cpy, 'inc': inc, 'dec': dec, 'jnz': jnz}

while pointer < len(lines):
    lijst = lines[pointer].split(' ')
    instr = lijst[0]
    argums = lijst[1:]

    result = functions[instr](*argums)

    if result is not None:
        pointer += result
    else:
        pointer += 1

print(REGISTERS['a'])
print(time.time() - start_time)
