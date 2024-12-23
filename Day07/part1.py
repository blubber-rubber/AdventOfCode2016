import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

p1 = r"(.)(.)\2\1"
p2 = r"\[[^[\]]*((.)(.)\3\2)[^[\]]*\]"
p3 = r"(.)\1\1\1"

score = 0
for line in lines:
    match1 = re.search(p1, line)
    if match1:
        match2 = re.search(p2, line)
        if not match2:
            group = match1.group()
            match3 = re.search(p3, group)
            if not match3:
                score += 1

print(score)
print(time.time() - start_time)
