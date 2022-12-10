import numpy as np

steps = []

with open('input9.txt', 'r') as f:
    for line in f:
        line = line.strip().split(' ')
        line[1] = int(line[1])
        steps.append(line)

# part 1

# let the starting position have the coordinates s = (0,0)

coordinates_H = [[0,0]]
coordinates_T = [[0,0]]
coordinates_s = [0,0]

def check_touch (H, T):
    if abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
        return False
    else: return True 

def do_step(step):
    global coordinates_H
    global coordinates_T
    if step[0] == 'R':
        for i in range(step[1]):
            coordinates_H.append(coordinates_H[-1].copy())
            coordinates_H[-1][0] += 1
            if not check_touch(coordinates_H[-1], coordinates_T[-1]):
                coordinates_T.append(coordinates_H[-1].copy())
                coordinates_T[-1][0] -= 1
    elif step[0] == 'U':
        for i in range(step[1]):
            coordinates_H.append(coordinates_H[-1].copy())
            coordinates_H[-1][1] += 1
            if not check_touch(coordinates_H[-1], coordinates_T[-1]):
                coordinates_T.append(coordinates_H[-1].copy())
                coordinates_T[-1][1] -= 1
    elif step[0] == 'L':
        for i in range(step[1]):
            coordinates_H.append(coordinates_H[-1].copy())
            coordinates_H[-1][0] -= 1
            if not check_touch(coordinates_H[-1], coordinates_T[-1]):
                coordinates_T.append(coordinates_H[-1].copy())
                coordinates_T[-1][0] += 1
    elif step[0] == 'D':
        for i in range(step[1]):
            coordinates_H.append(coordinates_H[-1].copy())
            coordinates_H[-1][1] -= 1
            if not check_touch(coordinates_H[-1], coordinates_T[-1]):
                coordinates_T.append(coordinates_H[-1].copy())
                coordinates_T[-1][1] += 1

for s in steps:
    do_step(s)

unique_coordinates = []

for i in coordinates_T:
    if i not in unique_coordinates:
        unique_coordinates.append(i.copy())

print(len(unique_coordinates))