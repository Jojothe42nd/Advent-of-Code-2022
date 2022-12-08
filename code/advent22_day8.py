import re
import numpy as np

forest = []

with open('input8.txt', 'r') as f:
    for line in f:
        line.strip()
        temp = re.findall(r'[0-9]', line)
        forest.append(temp)

ans = 0
R = len(forest)
C = len(forest[0])

# part 1

def check_visibility(r, c):
    global R
    global C
    global ans
    if r in [0, R]:
        ans += 1
    elif c in [0, C]:
        ans += 1 
    else:
        check_vis = [True, True, True, True]
        for rr in range(r):
            if int(forest[rr][c]) >= int(forest[r][c]):
                check_vis[0] = False
        for rr in range(r+1, R):
            if int(forest[rr][c]) >= int(forest[r][c]):
                check_vis[1] = False
        for cc in range(c):
            if int(forest[r][cc]) >= int(forest[r][c]):
                check_vis[2] = False
        for cc in range(c+1, C):
            if int(forest[r][cc]) >= int(forest[r][c]):
                check_vis[3] = False
        if (True in check_vis):
            ans += 1


for r in range(R):
    for c in range(C):
        check_visibility(r,c)

print(ans)

# part 2

score = [ [0]*C for i in range(R)]

def scenic_score (r,c):
    global score
    global R
    global C

    stop = [True, True, True, True]
    temp = [0] * 4
    rr = r-1
    while stop[0] and rr >= 0:
        if int(forest[rr][c]) < int(forest[r][c]):
            temp[0] += 1
        elif int(forest[rr][c]) >= int(forest[r][c]):
            temp[0] += 1
            stop[0] = False
        rr -= 1

    rr = r+1
    while stop[1] and rr < R:
        if int(forest[rr][c]) < int(forest[r][c]):
            temp[1] += 1
        elif int(forest[rr][c]) >= int(forest[r][c]):
            temp[1] += 1
            stop[1] = False
        rr += 1
    
    cc = c-1        
    while stop[2] and cc >= 0:
        if int(forest[r][cc]) < int(forest[r][c]):
            temp[2] += 1
        elif int(forest[r][cc]) >= int(forest[r][c]):
            temp[2] += 1
            stop[2] = False
        cc -= 1

    cc = c+1
    while stop[3] and cc < C:
        if int(forest[r][cc]) < int(forest[r][c]):
            temp[3] += 1
        elif int(forest[r][cc]) >= int(forest[r][c]):
            temp[3] += 1
            stop[3] = False
        cc += 1
    
    score[r][c] = np.prod(temp)




for r in range(R):
    for c in range(C):
        scenic_score(r,c)

maximum = np.max(score)
print (maximum)


# visualisation

import matplotlib.pyplot as plt

# tree hights

data = [list(map(int, r)) for r in forest]
fig, ax = plt.subplots()
ax1 = ax.imshow(data, cmap = 'Greens')
fig.colorbar(ax1)
ax.set_title('Tree Hight')
fig.savefig('tree_hights.png')

# scenic score

fig, ax = plt.subplots()
ax1 = ax.imshow(score, cmap = 'Blues')
fig.colorbar(ax1)
ax.set_title('Scenic score')
fig.savefig('scenic_score.png')