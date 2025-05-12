import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT'],
    'City': ['New York', 'San Francisco', 'Chicago', 'Boston', 'Seattle'],
    'Salary': [55000, 72000, 65000, 60000, 75000],          # Integer
    'Experience (Years)': [2, 4, 3, 5, 6]                    # Integer
}

df = pd.DataFrame(data)

print(df.describe())
print(df['Employee'])
print("The rows Employee and Department are selected and the coloumns 0 and 1 are selected")
print(df.iloc[0:2, 0:2])
print("Name and Department of Employees having Salary greater than 70000")
print(df[['Employee','Department']][df['Salary']>70000])
print("mean of Salary")
print([df['Salary']>df['Salary'].mean()])
print(df.head(2))
print(df.tail(2))

print(df.sort_values(by='Salary', ascending=False))
print(df.sort_values(by='Salary', ascending=True)) # ascending order
print(df.sort_values(by='Salary', ascending=False).head(2)) # top 2
print(df.sort_values(by='Salary', ascending=False).tail(2)) # bottom 2
print(" Name of Employees having Salary greater than maximum")
print(df['Employee'][df['Salary']==df['Salary'].max()]) # Name of Employees having Salary greater than maximum