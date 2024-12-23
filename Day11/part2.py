import re
import time
from heapq import heappop, heappush
from itertools import combinations
from collections import defaultdict
import math


def all_top_floor(state):
    for floor in state[:-1]:
        if len(floor) != 0:
            return False
    return True


def is_valid_state(state):
    for floor in state:
        chips = [c[:-1] for c in floor if c[-1] == 'C']
        generators = [g[:-1] for g in floor if g[-1] == 'G']
        for chip in chips:
            if len(generators) != 0 and chip not in generators:
                return False

    return True


def get_next_states(elevator_floor, state):
    possible_states = []
    for d_floor in [-1, 1]:
        new_floor_index = elevator_floor + d_floor
        if 0 <= new_floor_index < len(state):
            for moving_items in combinations(list(state[elevator_floor]) + [None], 2):
                floors = [list(f) for f in state]
                for m_item in moving_items:
                    if m_item is not None:
                        floors[elevator_floor].remove(m_item)
                        floors[new_floor_index].append(m_item)

                new_state = tuple(tuple(sorted(f)) for f in floors)
                if is_valid_state(new_state):
                    possible_states.append((new_floor_index, new_state))

    return possible_states


def heuristic_moves(elevator, state):
    score = abs(elevator - min(i for i, f in enumerate(state) if len(f) != 0))
    cum_sum = 0
    for floor in state[:-1]:
        cum_sum += len(floor)
        score += (cum_sum + 1) // 2

    return score


start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

starting_state = []

for i, line in enumerate(lines):
    content = []
    for m in re.finditer('a ([a-z]+) generator', line):
        content.append(m.groups()[0] + 'G')

    for m in re.finditer('a ([a-z]+)-compatible microchip', line):
        content.append(m.groups()[0] + 'C')

    if i == 0:
        content += ['eleriumG', 'eleriumC', 'dilithiumG', 'dilithiumC']

    starting_state.append(tuple(sorted(content)))

states = []
heappush(states, (heuristic_moves(0, starting_state), 0, 0, tuple(starting_state)))

print(starting_state)
visited = defaultdict(lambda: math.inf)

visited[(0, tuple(starting_state))] = 0

while states and not all_top_floor(states[0][3]):
    heuristic, n_moves, elevator_floor, floors = heappop(states)
    if n_moves <= visited[(elevator_floor, floors)]:
        for new_floor, new_state in get_next_states(elevator_floor, floors):
            if n_moves + 1 < visited[(new_floor, new_state)]:
                visited[(new_floor, new_state)] = 1 + n_moves
                heappush(states,
                         (n_moves + 1 + heuristic_moves(new_floor, new_state), n_moves + 1, new_floor, new_state))

print(states[0])
print(time.time() - start_time)
