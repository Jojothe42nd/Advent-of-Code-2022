import numpy as np

# part 1

elves = []
calories = []

with open('input1.txt', 'r') as f:
    for line in f:
        if line != '\n':
            calories.append(int(line))
        else:
            elves.append(calories)
            calories = []

length = max(map(len, elves))
elves = np.array([elve+[0]*(length-len(elve)) for elve in elves])

sum_calories = np.sum(elves, axis = 1)
print(max(sum_calories))

# part 2

sum_calories_sorted = np.sort(sum_calories)
top_three = sum(sum_calories_sorted[-3:])
print(top_three)
