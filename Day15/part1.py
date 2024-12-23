import time
import re
from functools import reduce
start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def find_inverse(a, m):
    for x in range(m):
        if (x * a) % m == 1:
            return x


def combine_equations(eq1, eq2):
    # x = a1 mod m1
    # x = a2 mod m2
    # x = k*m1 + a1
    # k  = m1^(-1)*(a2-a1) mod m2

    a1, m1 = eq1
    a2, m2 = eq2
    k = (find_inverse(m1 % m2, m2) * ((a2 - a1) % m2)) % m2

    return (k * m1 + a1, m1 * m2)


equations = []

for line in lines:
    string_match = re.match('Disc #([0-9]+) has ([0-9]+) positions; at time=0, it is at position ([0-9]+)', line)
    t, m, p = (int(x) for x in string_match.groups())
    equations.append((-(p + t) % m, m))

result = reduce(combine_equations, equations)

print(result[0])