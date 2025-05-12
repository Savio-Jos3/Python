import pandas as pd

data = [1,2,3]

print(pd.DataFrame(data))

data = {
    'Name': [1,2,3],
    'Age':  [4,5,6]
}

print(pd.DataFrame(data))

import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT'],
    'City': ['New York', 'San Francisco', 'Chicago', 'Boston', 'Seattle'],
    'Salary': [55000, 72000, 65000, 60000, 75000],          # Integer
    'Experience (Years)': [2, 4, 3, 5, 6]                    # Integer
}

df = pd.DataFrame(data)
print(df)
print(df[['Employee', 'Department']])

# Row Selection
print(df.iloc[0])
print("hee")
print(df.iloc[0,2]) # Row Selection based on index number
print(df.loc(0))    # Row Selection based on row name
print(df[['Salary']]) 
print(df[df['Salary']>100])
