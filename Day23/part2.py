import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in
             f.readlines()]  #.replace('inc a\ndec c\njnz c -2\ndec d\njnz d -5', 'mul c d a').split('\n')]

REGISTERS = {'a': 12, 'b': 0, 'c': 0, 'd': 0, 't': defaultdict(int)}

toggled = defaultdict(int)


def mul(x, y, z, pointer, registers=REGISTERS):
    if x in registers:
        x = registers[x]
    x = int(x)

    if y in registers:
        y = registers[x]
    y = int(y)
    registers[z] = x * y

    return pointer


def tgl(x, pointer, registers=REGISTERS):
    t = registers['t']
    if x in registers:
        x = registers[x]

    x = int(x)
    t[pointer + x] += 1

    return pointer


def cpy(x, y, pointer, registers=REGISTERS):
    if x in registers:
        registers[y] = registers[x]
    else:
        registers[y] = int(x)

    return pointer


def inc(x, pointer, registers=REGISTERS):
    registers[x] += 1
    return pointer


def dec(x, pointer, registers=REGISTERS):
    registers[x] -= 1
    return pointer


def jnz(x, y, pointer, registers=REGISTERS):
    if x in registers:
        x = registers[x]

    if y in registers:
        y = registers[y]

    if int(x) != 0:
        return pointer + int(y) - 1
    return pointer


pointer = 0

functions = {'cpy': cpy, 'inc': inc, 'dec': dec, 'jnz': jnz, 'tgl': tgl}
toggled_functions = {'cpy': jnz, 'inc': dec, 'dec': inc, 'jnz': cpy, 'tgl': inc}

all_functions = [functions, toggled_functions]

while pointer < len(lines):
    lijst = lines[pointer].split(' ')
    instr = lijst[0]
    argums = lijst[1:]

    if pointer == 5:
        REGISTERS['a'] += REGISTERS['c'] * REGISTERS['d']
        REGISTERS['c'] = 0
        REGISTERS['d'] = 0
        pointer += 5

    else:

        f = all_functions[REGISTERS['t'][pointer] % 2][instr]

        try:
            pointer = f(*argums, pointer)
        except Exception:
            pass
        finally:
            pointer += 1

print(REGISTERS['a'])
print(time.time() - start_time)

# 318020
# 9227674
