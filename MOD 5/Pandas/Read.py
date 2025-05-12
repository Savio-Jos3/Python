import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT'],
    'City': ['New York', 'San Francisco', 'Chicago', 'Boston', 'Seattle'],
    'Salary': [55000, 72000, 65000, 60000, 75000],          # Integer
    'Experience (Years)': [2, 4, 3, 5, 6]                    # Integer
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv')
print(df)
