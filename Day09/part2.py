import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

tape = lines[0]


def get_recursive_length(tape):
    length = 0
    i = 0
    while i < len(tape):
        if tape[i] == '(':
            i += 1
            data = ''
            while tape[i] != ')':
                data += tape[i]
                i += 1
            c, repeats = [int(x) for x in data.split('x')]
            characters = ''
            i += 1
            for _ in range(c):
                characters += tape[i]
                i += 1
            extra_length = get_recursive_length(characters)
            length += repeats * extra_length
        else:
            length += 1
            i += 1
    return length


length = get_recursive_length(tape)

print(length)
print(time.time() - start_time)
