from operator import inv
import numpy as np

A = np.array([[2,6],[4,8]])
B = np.array([[1,3],[2,4]])

C = A + B
print(C)
# C = A + B
C = np.add(A, B)
print(C) 

C = A - B
print(C)    
# C = A - B 
C = np.subtract(A, B)
print(C)
C = A * B
print(C)
# C = A * B
C = np.multiply(A, B)
print(C)
C = A / B
print(C)
# C = A / B

C = np.divide(A, B)
print(C)
C = A ** B
print(C)
# C = A ** B
C = np.power(A, B)      
print(C)
C = A @ B
print(C)

# C = A @ B
C = np.matmul(A, B)         
print(C)
C = np.dot(A, B)    
print(C)
# C = np.dot(A, B)
C = np.dot(A, B.T)
print(C)
# C = np.dot(A, B.T)
C = np.dot(A.T, B)
print(C)
# C = np.dot(A.T, B)    
C = np.dot(A.T, B.T)
print(C)        

C = inv(A)
print(C)
# C = inv(A)

