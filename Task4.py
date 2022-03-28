import numpy as np
# n = 6 k = 3
# 1 2 2 3 3 1
n, k = input().split(' ')
line = [int(el)for el in input().split(' ')]
price =[]
ind = []

def find_ind(list,el):
    indexes = []
    i = 0
    while i < len(list):
        if list[i] == el:
            indexes.append(i)
            i+=1
        else:
            i+=1
    return indexes


for el in range(1,int(k)+1):
    i = find_ind(line, el)
    ind.append(i)

import itertools as it

it = list(it.product(*ind))
sum = np.sum(line)
for l in it:
    if l[0] < l[-1]:
        new_sum = np.sum(line[l[0]:l[-1]+1])
    else:
        new_sum = np.sum(line[l[-1]:l[0]+1])
    if new_sum < sum:
        sum = new_sum
print(sum)

# search = line[ind[0]:ind[-1]+1]
# print(np.sum(search))

