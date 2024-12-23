import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

p1 = r"((^|])[^[\]]*(.)(.)\3.*\[[^\][]*\4\3\4[^\][]*\]|\[[^\][]*(.)(.)\5[^\][]*\].*\6\5\6[^[\]]*(\[|$))"

score = 0
for line in lines:

    match1 = re.search(p1, line)
    if match1:
        groups = match1.groups()
        if groups[2] != groups[3] or groups[4] != groups[5]:
            score += 1

print(score)
print(time.time() - start_time)
