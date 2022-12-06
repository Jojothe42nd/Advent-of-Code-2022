signal = []
with open('input6.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        signal = line


# part 1 and 2 

mess = ''

for i in range(len(signal[0])):
    if len(mess) == 14: # for part 1 change here to 4 and for part 2 change here to 14
        print(i)
        break
    if signal[0][i] in mess:
        mess = mess[mess.index(signal[0][i])+1:] + signal[0][i]
    elif signal[0][i] not in mess:
        mess += signal[0][i]
    print(mess)
