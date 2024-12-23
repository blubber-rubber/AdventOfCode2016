import time
from collections import defaultdict
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

v1 = 17
v2 = 61

BOTS = defaultdict(lambda: Bot())
OUTPUTS = defaultdict(lambda: Output())


class Output:

    def __init__(self):
        self.chips = []

    def give_chip(self, chip):
        self.chips.append(chip)


class Bot:

    def __init__(self):
        self.chips = []
        self.name = None
        self.upper = None
        self.lower = None

    def set_name(self, name):
        self.name = name

    def set_instructions(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def give_chip(self, chip):
        self.chips.append(chip)
        if len(self.chips) >= 2:

            self.chips.sort()
            l, u = self.chips

            if l == v1 and u == v2:
                print(self.name)

            self.chips = []
            self.lower.give_chip(l)
            self.upper.give_chip(u)


for line in lines:
    m = re.match('bot ([0-9]*) gives low to (bot|output) ([0-9]*) and high to (bot|output) ([0-9]*)', line)
    if m:

        b, t1, b1, t2, b2 = m.groups()
        bot = BOTS[b]

        if t1 == 'bot':
            low = BOTS[b1]
            low.set_name(b1)
        else:
            low = OUTPUTS[b1]

        if t2 == 'bot':
            high = BOTS[b2]
            high.set_name(b2)
        else:
            high = OUTPUTS[b2]

        bot.set_instructions(low, high)

for line in lines:
    m = re.match('value ([0-9]*) goes to bot ([0-9]*)', line)
    if m:
        v, b = m.groups()
        bot = BOTS[b]
        bot.set_name(b)
        bot.give_chip(int(v))

print(time.time() - start_time)
