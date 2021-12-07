# import numpy as np
#  Opening file in read mode...
f = open('test2.txt', 'r')
# Reading no. of rows(and col's)...
rows_1 , col_1 = [int(x) for x in f.readline().strip().split(' ')]
# print(rows_1, col_1)
# reading 1st matrix....
M_1 = []
for line in f:
    r = line.strip()
    if r:
        M_1 += [[int(a) for a in r.split(' ')]]
    else:   break

rows_2 , col_2 = [int(x) for x in f.readline().strip().split(' ')]
# print(rows_2, col_2)
# reading 1st matrix....
M_2 = []
for line in f:
    r = line.strip()
    if r:
        M_2 += [[int(a) for a in r.split(' ')]]
    else:   break

f.close()
print(M_1, M_2)

prod = [ [0 for c in range(col_2)] for i in range(rows_1) ]
print(prod)
if col_1 == rows_2:
    for i in range(rows_1):
        # prod.append([])
        for j in range(col_2):
            # prod[i].append(0)
            for k in range(rows_2):
                print(i, j, k)
                prod[i][j] += M_1[i][k] * M_2[k][j]

else: print('Matrix are of INVALID sizes.')

print(prod)