from collections import OrderedDict

import numpy as np

SIZE = int(input("Input number of points: "))
GO_FROM = int(input("Input start point: "))
GO_TO = int(input("Input end point: "))

data = np.zeros((SIZE, SIZE), dtype=int)
for i in range(SIZE):
    for j in range(SIZE):
        if i == j:
            continue
        data[i, j] = int(input(f'Input {i+1} - {j+1} distance: '))

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
        if data[current_point][i] != 0 and weights[i] > data[current_point][i] + weights[current_point]:
                weights[i] = data[current_point][i] + weights[current_point]
    to_visit.remove(current_point)

print(f'Shortest distances to points from {GO_FROM}:')

for i in weights:
    print(i + 1, ": ", weights[i], sep='', end='\t')

print(f'\nShortest path from {GO_FROM} to {GO_TO}:')

path = [GO_TO]
curr = int(weights[GO_TO - 1])
curr_position = GO_TO - 1
while curr > 0:
    for i in range(SIZE):
        if data[i][curr_position] != 0 and curr - data[i][curr_position] == weights[i]:
                path.append(i+1)
                curr -= data[i][curr_position]
                curr_position = i
                break
    else:
        print("ERROR")
        exit(1)

for i in reversed(path):
    print(i, end=' ')
    if i != GO_TO:
        print("=> ", end='')
