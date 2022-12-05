import re

# part 1

stack = []
position = []
crane = []

with open ('input5.txt', 'r') as f:
    for line in f:
        if line[0] == '[':
            stack.append(line.strip())
        elif line[0] == ' ':
            position.append(line.strip())
        elif line[0] == 'm':
            line_num = re.findall(r'[0-9]+', line)
            crane.append(line_num)

stack = stack[::-1]
stack_vert = ['']*len(stack[0])

for i in range(len(stack)):
    for j in range(len(stack[i])):
        if stack[i][j] != '[' and stack[i][j] != ']' and stack[i][j]!= ' ':
            stack_vert[j] += stack[i][j]

stack_vert = list(filter(None, stack_vert))
stack_Vert = stack_vert.copy()


for i in range(len(crane)): 
    for j in range(int(crane[i][0])):
        stack_vert[int(crane[i][2])-1] += stack_vert[int(crane[i][1])-1][-j-1]
    stack_vert[int(crane[i][1])-1] = stack_vert[int(crane[i][1])-1][:-int(crane[i][0])]

solution = ''
for x in stack_vert:
    solution += x[-1]

print(solution)


# part 2

stack_vert = stack_Vert.copy()

for i in range(len(crane)): 
    stack_vert[int(crane[i][2])-1] += stack_vert[int(crane[i][1])-1][-int(crane[i][0]):]
    stack_vert[int(crane[i][1])-1] = stack_vert[int(crane[i][1])-1][:-int(crane[i][0])]

solution = ''
for x in stack_vert:
    solution += x[-1]

print(solution)