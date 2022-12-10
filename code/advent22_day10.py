import numpy as np

input = []

with open('input10.txt') as f:
    for line in f:
        line = line.strip().split()
        input.append(line)

# part 1

x = 1
cycle = 0
signal_strength = []


for i in input:
    if i[0] == 'noop':
        cycle += 1
        if cycle % 40 == 20:
            signal_strength.append(cycle * x)
    if i[0] == 'addx':
        for j in range(2):
            cycle += 1
            if cycle % 40 == 20: 
                signal_strength.append(cycle * x)
        x += int(i[1])

print(sum(signal_strength))

# part 2

cycle = 0
x = 1
crt = [[None]*40 for i in range(6)]

for i in input:
    if i[0] == 'noop':
        if x-1 <= cycle%40 <= x+1:
            crt[cycle//40][cycle%40] = '\u2588'
        else:
            crt[cycle//40][cycle%40] = '.'
        cycle += 1
    if i[0] == 'addx':
        for j in range(2):
            if x-1 <= cycle%40 <= x+1:
                crt[cycle//40][cycle%40] = '\u2588'
            else:
                crt[cycle//40][cycle%40] = '.'
            cycle += 1
        x += int(i[1])

with open('output.txt', 'w', encoding='utf8') as f:
    for line in crt:
        for char in line:
            f.write(char)
        f.write('\n')
