"""Write a python program to create two numpy arays of random integers between
0 and 20 of shape (3, 3) and perform matrix addition, multiplication and transpose
 of the product matrix."""

import numpy as np
# Create two numpy arrays of random integers between 0 and 20 of shape (3, 3)

A = np.random.randint(0, 20, size =(3,3))

print("Matrix A:")
print(A)

print(A-A)
print(A.dot(A))
print(A.T)
