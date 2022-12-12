from collections import defaultdict
from collections import deque

height = []

with open('input12.txt', 'r') as f:
    for line in f:
        height.append([])
        line = line.strip()
        for char in line:
            height[-1].append(char)

height2 = [[0 for _ in range(len(height[0]))] for _ in range(len(height))]
for y in range(len(height)):
    for x in range(len(height[0])):
        if height[y][x]=='S':
            height2[y][x] = 1
        elif height[y][x] == 'E':
            height2[y][x] = 26
        else:
            height2[y][x] = ord(height[y][x])-ord('a')+1


def shortest_path (start, goal):
    global height
    global height2

    explored = set()
    queue = deque()
    queue.append((start,0))
    
    if height[start[1]][start[0]] == goal:
        print('E is the same as S')
        return ['E']

    while queue:
        
        (x, y), d = queue.popleft()

        if (x,y) in explored:
            continue

        explored.add((x, y))

        if height[y][x] == goal:
            print('Found the shortest path.')
            return d
        for dx, dy in [(0,1), (1,0), (0, -1), (-1,0)]:
                xx = x+dx
                yy = y+dy
                if 0 <= xx < len(height[y]) and 0 <= yy < len(height):
                    if height2[yy][xx]<=1+height2[y][x] and (xx, yy) not in explored:
                        queue.append(((xx, yy), d+1))

for i in range(len(height)):
    for j in range(len(height[i])):
        if height[i][j] == 'S':
            y_s, x_s = i, j
        if height[i][j] == 'E':
            y_e, x_e = i, j


print(shortest_path((x_s, y_s), 'E'))

def shortest_path2 (start, goal):
    global height
    global height2

    explored = set()
    queue = deque()
    queue.append((start,0))
    
    if height[start[1]][start[0]] == goal:
        print('E is the same as S')
        return ['E']

    while queue:
        
        (x, y), d = queue.popleft()

        if (x,y) in explored:
            continue

        explored.add((x, y))

        if height[y][x] == goal:
            print('Found the shortest path.')
            return d
        for dx, dy in [(0,1), (1,0), (0, -1), (-1,0)]:
                xx = x+dx
                yy = y+dy
                if 0 <= xx < len(height[y]) and 0 <= yy < len(height):
                    if height2[yy][xx]+1>=height2[y][x] and (xx, yy) not in explored:
                        queue.append(((xx, yy), d+1))

print(shortest_path2((x_e, y_e), 'a'))