import numpy as np

rock = []

with open ('input14.txt', 'r') as f:
    for line in f :
        line = line.strip().split(' -> ')
        temp = []
        for l in line:
            temp.append(l.split(','))

        rock.append([[int(t) for t in subtemp] for subtemp in temp])

# part 1

cave = set()

for r in range(len(rock)):
    prev = None
    for i in range(len(rock[r])):
        x, y = rock[r][i]
        if prev is not None:
            if x-prev[0] == 0:
                for dy in range(abs(y-prev[1])+1):
                    xx = x
                    yy = prev[1]+dy*(1 if y-prev[1]>0 else (-1 if y-prev[1]<0 else 0))
                    cave.add((xx,yy))
            elif y-prev[1] == 0:
                for dx in range(abs(x-prev[0])+1):
                    yy = y
                    xx = prev[0]+dx*(1 if x-prev[0]>0 else (-1 if x-prev[0]<0 else 0))
                    cave.add((xx,yy))
        prev = x,y

floor = max(c[1] for c in cave) - 1


for i in range(1000):
    sand = (500, 0)
    can_fall = True
    abyss = False
    while can_fall:  
        if sand[1]> floor:
            abyss = True
            break
        if (sand[0], sand[1]+1) not in cave:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in cave:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in cave:
            sand = (sand[0]+1, sand[1]+1)
        else:
            can_fall = False
    if abyss:
        print(i)
        break
    cave.add(sand)

# part 2

cave = set()

for r in range(len(rock)):
    prev = None
    for i in range(len(rock[r])):
        x, y = rock[r][i]
        if prev is not None:
            if x-prev[0] == 0:
                for dy in range(abs(y-prev[1])+1):
                    xx = x
                    yy = prev[1]+dy*(1 if y-prev[1]>0 else (-1 if y-prev[1]<0 else 0))
                    cave.add((xx,yy))
            elif y-prev[1] == 0:
                for dx in range(abs(x-prev[0])+1):
                    yy = y
                    xx = prev[0]+dx*(1 if x-prev[0]>0 else (-1 if x-prev[0]<0 else 0))
                    cave.add((xx,yy))
        prev = x,y

floor = max(c[1] for c in cave) +2
left = min(c[0] for c in cave) -100000
right = max(c[0] for c in cave) +100000



for i in range(left, right):
    cave.add((i, floor))

for i in range(100000):
    sand = (500, 0)
    can_fall = True
    while can_fall:  
        if (sand[0], sand[1]+1) not in cave:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in cave:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in cave:
            sand = (sand[0]+1, sand[1]+1)
        else:
            can_fall = False
    if sand == (500, 0):
        print(i+1)
        break
    cave.add(sand)