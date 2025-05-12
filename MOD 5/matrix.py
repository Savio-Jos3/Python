import numpy as np

matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        val= int(input())
        row.append(val)
    matrix.append(row)
mat = np.array(matrix)
print(matrix)
print(mat)
