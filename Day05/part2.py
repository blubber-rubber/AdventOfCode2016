import time
import hashlib

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

door_id = lines[0]

password = [None] * 8
index = 0
missing = set(str(i) for i in range(8))

while missing:
    result = hashlib.md5(f'{door_id}{index}'.encode('ASCII')).hexdigest()
    if result.startswith('00000') and result[5] in missing:
        missing.remove(result[5])
        password[int(result[5])] = result[6]
    index += 1

print(''.join(password))

print(time.time() - start_time)
