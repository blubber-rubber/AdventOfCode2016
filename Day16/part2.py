import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

bits = lines[0]
disk_length = 35651584

while len(bits) < disk_length:
    bits = bits + '0' + ''.join('0' if b == '1' else '1' for b in reversed(bits))

bits = bits[:disk_length]

while len(bits) % 2 == 0:
    bits = ''.join(str(int(bits[2 * i] == bits[2 * i + 1])) for i in range(len(bits) // 2))

print(bits)
print(time.time() - start_time)
