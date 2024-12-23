import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

tape = lines[0]

i = 0

decompressed = ''
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
        decompressed += characters * repeats
    else:
        decompressed += tape[i]

        i += 1

print(len(decompressed))
print(time.time() - start_time)
