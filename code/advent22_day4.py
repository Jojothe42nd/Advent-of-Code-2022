import re

# part 1

elve1 = []
elve2 = []

with open('input4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        elve1.append(re.findall(r'\d+',line[0])[:2])
        elve2.append(re.findall(r'\d+',line[0])[2:])

for elve in elve1:
    elve[0] = int(elve[0])
    elve[1] = int(elve[1])

for elve in elve2:
    elve[0] = int(elve[0])
    elve[1] = int(elve[1])

num_same = 0
for i in range(len(elve1)):
    if elve1[i][0] >= elve2[i][0] and elve1[i][1] <= elve2[i][1]:
        num_same += 1
    elif elve2[i][0] >= elve1[i][0] and elve2[i][1] <= elve1[i][1]:
        num_same += 1

print(num_same)

# part 2

num_same2 = 0
for i in range(len(elve1)):
    if elve1[i][0] >= elve2[i][0] and elve1[i][0] <= elve2[i][1]:
        num_same2 += 1
    elif elve1[i][1] >= elve2[i][0] and elve1[i][1] <= elve2[i][1]:
        num_same2 += 1
    elif elve2[i][0] >= elve1[i][0] and elve2[i][0] <= elve1[i][1]:
        num_same2 += 1
    elif elve2[i][1] >= elve1[i][0] and elve2[i][1] <= elve1[i][1]:
        num_same2 += 1

print(num_same2)