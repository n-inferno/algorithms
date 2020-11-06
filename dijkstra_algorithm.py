import numpy as np
from collections import OrderedDict

SIZE = int(input("Input number of points: "))
GO_FROM = int(input("Input start point: "))
GO_TO = int(input("Input end point: "))

data = np.zeros((SIZE, SIZE), dtype=int)
for i in range(SIZE):
    for j in range(i + 1, SIZE):
        data[i, j] = int(input(f'Input {i+1} - {j+1} distance: '))
        data[j, i] = data[i, j]

to_visit = [i for i in range(SIZE)]
weights = OrderedDict()

for i in range(SIZE):
    if i == GO_FROM - 1:
        weights[i] = 0
    else:
        weights[i] = float('inf')

while to_visit:
    current_point = min([i for i in weights.keys() if i in to_visit], key=lambda x: weights[x])
    for i in range(SIZE):
        if data[current_point][i] != 0:
            if weights[i] > data[current_point][i] + weights[current_point]:
                weights[i] = data[current_point][i] + weights[current_point]
    to_visit.remove(current_point)

print(f'Shortest distances to points from {GO_FROM}:')

for i in weights:
    print(i + 1, ": ", weights[i], end='\t')

print(f'\nShortest path from {GO_FROM} to {GO_TO}:')

path = [GO_TO]
curr = weights[GO_TO - 1]
curr_position = GO_TO - 1
while curr > 0:
    for i in range(SIZE):
        if data[curr_position][i] != 0:
            if curr - data[curr_position][i] == weights[i]:
                path.append(i+1)
                curr -= data[curr_position][i]
                curr_position = i
                break
    else:
        print("ERROR")

for i in reversed(path):
    print(i, end=' ')
    if i != GO_TO:
        print("=> ", end='')