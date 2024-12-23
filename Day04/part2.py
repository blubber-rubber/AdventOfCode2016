import time
from collections import Counter

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def decipher(words, sector_id):
    shift = sector_id % 26
    name = ""
    for word in words:
        for char in word:
            name += ALPHABET[(ALPHABET.find(char) + shift) % 26]
        name += " "
    return name.rstrip(' ')


for line in lines:
    name, checksum = line.split('[')
    name, checksum = name.split('-'), checksum.rstrip(']')
    room_name, sector_id = name[:-1], int(name[-1])
    c = Counter(''.join(room_name))
    if checksum == ''.join(sorted(c, key=lambda x: (-c[x], x)))[:5]:
        if decipher(room_name, sector_id) == 'northpole object storage':
            print(sector_id)

print(time.time() - start_time)
