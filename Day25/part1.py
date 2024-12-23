import time


start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


"""
Today's solution was found by manually analyzing the input.txt file

the input file did the following function

"""


def loop_once(a):
    rem = 2550 + a
    outputs = []
    while rem != 0:
        outputs.append(rem % 2)
        rem = rem // 2

    return outputs


def check_loop(loop):
    return len(loop) % 2 == 0 and all(sum(p) == 1 for p in zip(loop, loop[1:]))


a = 0

while not check_loop(loop_once(a)):
    a += 1

print(a)
print(time.time() - start_time)
