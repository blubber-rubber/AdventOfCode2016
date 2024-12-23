import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

current_row = lines[0]

rows = [current_row]


def get_relevant(row, index):
    if index == 0:
        return '.' + row[:2]
    if index + 1 == len(row):
        return row[-2:] + '.'

    return row[index - 1:index + 2]


counter = len([c for c in current_row if c == '.'])

while len(rows) < 40:

    new_row = ''
    for index in range(len(current_row)):
        relevant = get_relevant(current_row, index)
        if relevant in ('^^.', '.^^', '^..', '..^'):
            new_row += '^'
        else:
            counter += 1
            new_row += '.'

    rows.append(new_row)
    current_row = new_row

print(counter)
print(time.time() - start_time)
