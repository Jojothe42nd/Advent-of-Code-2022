import re
monkey = []
operation = []
test = []
test_true = []
test_false = []

with open('input11.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if 'Starting items' in line:
            monkey.append([int(i) for i in re.findall(r'[0-9]+', line)])
        elif 'Operation' in line:
            operation.append(line.split('new = ')[1])  
        elif 'Test' in line:
            test.append(int(re.findall(r'[0-9]+', line)[0]))
        elif 'true' in line:
            test_true.append(int(re.findall(r'[0-9]+', line)[0]))
        elif 'false' in line:
            test_false.append(int(re.findall(r'[0-9]+', line)[0]))

activity = [0] * len(monkey)
manage = 1
for i in test:
    manage *=  i

def monkey_turn(m):
    global monkey
    global operation
    global test
    global test_false
    global test_true
    global activity

    I = len(monkey[m])
    for i in range(I):
        activity[m] += 1
        if '* old' in operation[m]:
            monkey[m][i] = monkey[m][i]*monkey[m][i] // 3
        if ' + ' in operation[m]:
            plus = int(re.findall(r'[0-9]+', operation[m])[0])
            monkey[m][i] = (monkey[m][i] + plus) // 3
        if ' * ' in operation[m] and not '* old' in operation[m]:
            times = int(re.findall(r'[0-9]+', operation[m])[0])
            monkey[m][i] = (monkey[m][i] * times) // 3

        if monkey[m][i] % test[m] == 0:
            monkey[test_true[m]].append(monkey[m][i])
        elif monkey[m][i] % test[m] != 0:
            monkey[test_false[m]].append(monkey[m][i])
    monkey[m] = []
            

def part1 ():
    M = len(monkey)
    R = 20

    for r in range(R):
        for m in range(M):
            monkey_turn(m)

    print(activity)
    activity.sort()
    business = activity[-2] * activity[-1]
    print(business)

# part 2


def monkey_turn2(m):
    global monkey
    global operation
    global test
    global test_false
    global test_true
    global activity
    global manage

    I = len(monkey[m])
    for i in range(I):
        activity[m] += 1
        if '* old' in operation[m]:
            monkey[m][i] = (monkey[m][i]*monkey[m][i]) 
        if ' + ' in operation[m]:
            plus = int(re.findall(r'[0-9]+', operation[m])[0])
            monkey[m][i] = (monkey[m][i] + plus) 
        if ' * ' in operation[m] and not '* old' in operation[m]:
            times = int(re.findall(r'[0-9]+', operation[m])[0])
            monkey[m][i] = (monkey[m][i] * times)

        if monkey[m][i] % test[m] == 0:
            monkey[test_true[m]].append(monkey[m][i] % manage)
        elif monkey[m][i] % test[m] != 0:
            monkey[test_false[m]].append(monkey[m][i] % manage)
    monkey[m] = []
            

def part2():
    M = len(monkey)
    R = 10000

    for r in range(R):
        for m in range(M):
            monkey_turn2(m)

    print(activity)
    activity.sort()
    business = activity[-2] * activity[-1]
    print(business)

part2()