left = []
right = []

part1 = 0

with open('input13_lw.txt', 'r') as f:
    for line in f:
        if line == '\n':
            continue
        left.append(eval(line.strip()))
        right.append(eval(f.readline().strip()))

def compare (l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l == r:
            return 0
        else:
            return 1
    elif isinstance(l, list) and isinstance(r, list):
        i = 0
        while i < len(l) and i < len(r):
            if compare(l[i], r[i]) == -1:
                return -1
            if compare(l[i], r[i]) == 1:
                return 1
            i += 1
        if i == len(l) and i < len(r):
            return -1
        elif i == len(r) and i < len(l):
            return 1
        else:
            return 0
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    else:
        return compare([l], r)


for l in range(len(left)):
    if compare(left[l], right[l]) == -1:
        part1 += l+1

print(part1)

packets = []
for l in range(len(left)):
    packets.append(left[l])
    packets.append(right[l])

packets.append([[2]])
packets.append([[6]])



from functools import cmp_to_key

compare_key = cmp_to_key(compare)
packets_sorted = sorted(packets, key = compare_key(lambda left, right: compare(left, right)))

part2 = 1

for p in range(len(packets_sorted)):
    if packets_sorted[p] == [[2]] or packets_sorted[p] == [[6]]:
        part2 *= p+1

print(part2)