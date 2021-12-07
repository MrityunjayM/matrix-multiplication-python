# import numpy as np
#  Opening file in read mode...
f = open('test1.txt', 'r')
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
# print(M_1, M_2)
# Creating zero matrix with expected product matrix dimension.
prod = [ [0 for c in range(col_2)] for i in range(rows_1) ]
# Multiplying matrix 1 with 2.
if col_1 == rows_2:
    for i in range(rows_1):
        for j in range(col_2):
            for k in range(rows_2):
                # Calculating....
                prod[i][j] += M_1[i][k] * M_2[k][j]
# Warning in case of dimension mis-match.
else: print('Matrix are of INVALID sizes.')
# OUTPUT: Printing the product matrix.
print(prod)
# ~~~ END ~~~