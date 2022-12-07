direc = ['/']
size = [0]

import numpy as np

# part 1

with open('input7.txt', 'r') as f:
    f.readline()
    work_direc = ['/']
    for line in f:
        path = work_direc[-1]
        line = line.strip().split(' ')
        if line[0] == 'dir' and path+'/'+line[1] not in direc:
            direc.append(path+'/'+line[1])
            size.append(0)
        elif line[1] == 'cd' and '..' not in line:
            work_direc.append(path + '/' + line[2])
        elif line[0].isnumeric():
            for d in work_direc:
                size[direc.index(d)] += int(line[0])
        elif '..' in line:
            work_direc.pop()
    
ans = 0
for i in size:
    if i <= 100000:
        ans += i
print(ans)

# part 2
diff = - (70000000 - 30000000 - size[0])

direc_diff = []
poss_direc = []

for d in range(len(direc)):
    direc_diff.append(size[d] - diff)
    if size[d]-diff >= 0:
        poss_direc.append(size[d]-diff)

diff_min = min(poss_direc)
direc_min_ind = direc_diff.index(diff_min)
size_min = size[direc_min_ind]

print(size_min)
