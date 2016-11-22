#Secret Santa Helper
#Randomly order people in one chain so that no person gives to someone in the
#same group

import random
import sys

answer = []
data_in = []
formatting = 0
total = 0
longest = 0

with open('input.txt') as read:
    for r in read.read().splitlines():
        if '-' in r:
            if data_in and len(data_in[-1]) > longest:
                longest = len(data_in[-1])
            data_in.append([])
        else:
            if len(r) > formatting:
                formatting = len(r)
            data_in[-1].append(r)
            total += 1
    if len(data_in[-1]) > longest:
        longest = len(data_in[-1])

if float(longest) / total > 0.5:
    with open('output.txt', 'w') as w:
        w.write('No possible permutation given inputs.\n')
        w.write('Largest department cannot be more than half of population')
    sys.exit(1)

data_in = sorted(data_in, key=len, reverse=True)
[random.shuffle(i) for i in data_in]

while True:
    last = data_in[0]
    answer.append(data_in[0][0])
    del data_in[0][0]
    if len(data_in[0]) == 0:
        del data_in[0]
    if len(data_in) == 0:
        break
    data_in = sorted(data_in, key=len, reverse=True)
    if len(data_in) != 1 and last == data_in[0]:
        temp = data_in[0]
        data_in[0] = data_in[1]
        if len(data_in[0]) != 1:
            data_in[1] = data_in[-1]
            data_in[-1] = temp
        else:
            data_in[1] = temp

with open('output.txt', 'w') as w:
    for i in range(len(answer)):
        w.write(answer[i].ljust(formatting) + ' gives to ' + 
                answer[(i+1)%len(answer)] + '\n')
