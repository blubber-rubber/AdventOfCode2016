import time
from itertools import permutations

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

scramble = [c for c in 'abcde']

import re


def rotate_left(lijst, n):
    n = int(n)
    return lijst[n % len(lijst):] + lijst[:n % len(lijst)]


def rotate_right(lijst, n):
    return lijst[-int(n) % len(lijst):] + lijst[:-int(n) % len(lijst)]


def swap(lijst, x, y):
    x, y = int(x), int(y)
    lijst[x], lijst[y] = lijst[y], lijst[x]
    return lijst


def move(lijst: list, x, y):
    e = lijst.pop(int(x))
    lijst.insert(int(y), e)
    return lijst


def rotation_based(lijst, s):
    i = lijst.index(s)
    return rotate_right(lijst, 1 + i + (i >= 4))


def reverse(lijst, x, y):
    x, y = int(x), int(y)
    return lijst[:x] + lijst[x:y + 1][::-1] + lijst[y + 1:]


def swap_letters(lijst, x, y):
    return swap(lijst, lijst.index(x), lijst.index(y))


scramble = list('abcdefgh')

# scramble = swap(scramble, 4, 0)
# print(scramble)
#
# scramble = swap_letters(scramble, 'd', 'b')
# print(scramble)
#
# scramble = reverse(scramble, 0, 4)
# print(scramble)
#
# scramble = rotate_left(scramble, 1)
# print(scramble)
#
# scramble = move(scramble, 1, 4)
# print(scramble)
#
# scramble = move(scramble, 3,0 )
# print(scramble)
#
#
# scramble = rotation_based(scramble, 'b')
# print(scramble)
#
# scramble = rotation_based(scramble, 'd')
# print(scramble)

patterns = list({'rotate right (.*) steps?': rotate_right,
                 'swap letter (.*) with letter (.*)': swap_letters,
                 'move position (.*) to position (.*)': move,
                 'swap position (.*) with position (.*)': swap,
                 'rotate based on position of letter (.*)': rotation_based,
                 'reverse positions (.*) through (.*)': reverse,
                 'rotate left (.*) steps?': rotate_left
                 }.items())

for perm in permutations('abcdefgh'):
    scramble = list(perm)

    for line in lines:
        index = 0
        m = None
        while m is None:
            pattern, f = patterns[index]
            m = re.match(pattern, line)
            index += 1

        scramble = f(scramble, *m.groups())

    if ''.join(scramble) == 'fbgdceah':
        print(''.join(perm))
print(time.time() - start_time)
