# part 1

rounds = []
with open('input2.txt', 'r') as f:
    for line in f:
        rounds.append(line.strip())

ldw = {'l':0, 'd': 3, 'w':6}
rps = {'r':1, 'p':2, 's': 3}
points = {'A X': ldw['d'] + rps['r'], 'A Y': ldw['w'] + rps['p'], 'A Z': ldw['l'] + rps['s'],
         'B X': ldw['l'] + rps['r'], 'B Y': ldw['d'] + rps['p'], 'B Z': ldw['w'] + rps['s'],
         'C X': ldw['w'] + rps['r'], 'C Y': ldw['l'] + rps['p'], 'C Z': ldw['d'] + rps['s']}

points_rounds = []
for i in rounds:
    points_rounds.append(points[i])
    
sum_points = sum(points_rounds)
print(sum_points)

# part 2

ldw2 = {'X':0, 'Y': 3, 'Z':6}

l = {'A':'s', 'B':'r', 'C':'p'}
d = {'A':'r', 'B':'p', 'C':'s'}
w = {'A':'p', 'B':'s', 'C':'r'}

points_rounds2 = []
for i in rounds:
    temp_points = ldw2[i[2]]
    if i[2] == 'X':
        temp_points += rps[l[i[0]]]
    elif i[2] == 'Y':
        temp_points += rps[d[i[0]]]
    elif i[2] == 'Z':
        temp_points += rps[w[i[0]]]
    points_rounds2.append(temp_points)

sum_points2 = sum(points_rounds2)
print(sum_points2)