import string

# part 1

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

rucksacks = []
with open('input3.txt', 'r') as f:
    for line in f:
        line = line.strip()
        rucksacks.append(line)
        
compartments = []
for i in range(len(rucksacks)):
    half_len = int(len(rucksacks[i])/2)
    compartments.append(rucksacks[i][:half_len])
    compartments.append(rucksacks[i][half_len:])

double_item = []    
value_item = []

for i in range(0, len(compartments), 2):
    for j in range(len(compartments[i])):
        if compartments[i][j] in compartments[i+1]:
            double_item.append(compartments[i][j])
            value_item.append(values[compartments[i][j]])
            break

sum_prio = sum(value_item)
print(sum_prio)

# part 2

badges = []
value_badges = []

for i in range(0, len(rucksacks), 3):
    for j in range(len(rucksacks[i])):
        if rucksacks[i][j] in rucksacks[i+1] and rucksacks[i][j] in rucksacks[i+2]:
            badges.append(rucksacks[i][j])
            value_badges.append(values[rucksacks[i][j]])
            break
            
sum_badges = sum(value_badges)
print(sum_badges)