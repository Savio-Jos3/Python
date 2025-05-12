import numpy as np

A = np.arange(9, size = 3)
B = A.reshape(3,3)

#INDEXING
print("Indexing")
print(A[0]) # 0
print(B[0]) # 1

#SLICING
print("Slicing")
print(A[0:3])
print(B[0:2][1:2])# 
print(A[0:8:3])# 0 3 6
print(A[0:8:1])# 0 1 2 3 4 5 6 7
print(A[0:8:2])# 0 2 4 6 
print(A[0:8:1])# 0 1 2 3 4 5 6 7
print(A)
print(B)

slice = A[0:3]
slice = 100
print(A[0:3]) # 0 1 2   
print(slice) # 100 100 100
slice[:] = 200
print(A[0:3]) # 200 200 200
print(slice) # 200 200 200