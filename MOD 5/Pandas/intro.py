import pandas as pd

A = pd.Series([1, 2, 3, 4, 5])
print(A)

A = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(A)    

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A = pd.Series(dict) 
print(A)
A = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='numbers')
print(A)

A = pd.isnull([1, 2, 3, None])
print(A)

print("Mean is ", A.mean())
print("Head is", A.head())
print(A.values)