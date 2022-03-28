# sides = [input().split(' ')]
# # for el in range(6):
# #      a = int(input())
# #      sides.append(a)
# k = int(input())
#
import numpy as np
# result = []
# for el in range(k):
#     b = np.random.choice(sides)
#     result.append(b)
# print(result)
# ind = 1
# while ind < len(result):
#     try:
#         if result[-ind] == result[-ind-1]:
#             del result[-ind]
#         else:
#             ind+=1
#     except IndexError:
#         pass
sides = [int(a) for a in input().split()]
k = int(input())
#sides = [1, 2, 3, 4, 5, 6]
#k = 2
d = {}
for el in sides:
    d[el] = sides.count(el)
ps = []
for p in range(k-1):
    po = []
    for key, value in d.items():
        p = (value/6)**2*key
        po.append(p)
    ps.append(np.sum(po))

print(k*np.sum(sides)/6 - np.sum(ps))
# print(np.mean(result))