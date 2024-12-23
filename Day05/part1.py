import time
import hashlib

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

door_id = lines[0]

password = ''
index = 0

while len(password) < 8:
    result = hashlib.md5(f'{door_id}{index}'.encode('ASCII')).hexdigest()
    if result.startswith('00000'):
        password += result[5]
    index += 1

print(password)

print(time.time() - start_time)
