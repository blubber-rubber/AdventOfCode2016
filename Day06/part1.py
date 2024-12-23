import time
import numpy as np
from collections import Counter

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

columns = np.array([[c for c in line] for line in lines]).T

print(''.join(Counter(column).most_common()[0][0] for column in columns))

print(time.time() - start_time)
