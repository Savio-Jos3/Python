"""Write Pyhon program to write the data given below to a CSV file named student.csv
 fields : ['Name', 'Branch', 'Year', 'CGPA']

 rows 
: [ [Nikhil"'CSE"'2"'9.0'1],
 ['Sanchit"'CSE,'2"'9.1'1],
 
['Aditya','IT,'2','9.3'1],
 ['Sagar','IT','l','9.5]]
 b) Considerthe above studentcsv file with fields Name, Branch, Year, CGPA. (10)
 Write python code using pandas to
 l) To find the average CGPA ofthe students
 2) To display the details of all students having CGPA > 9
 3) To display the details of all CSE students with CGPA > 9
 4) To display the details of student with maximum CGPA
 5) To display average CGPA of each branch"""


import pandas as pd
data = {
    'Name': ['Nikhil', 'Sanchit', 'Aditya', 'Sagar'],
    'Branch': ['CSE', 'CSE', 'IT', 'IT'],
    'Year': [2, 2, 2, 1],
    'CGPA': [9.0, 9.1, 9.3, 9.5]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('student.csv', index = False)

print("Average CGPA of the students: ", df['CGPA'].mean())  
print("Details of all students having CGPA > 9: ")
print(df[df['CGPA'] > 9])
print("Details of all CSE students with CGPA > 9: ")
print(df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)])
print("Details of student with maximum CGPA: ") 
print(df[df['CGPA'] == df['CGPA'].max()])
print("Average CGPA of each branch: ")
print(df.groupby('Branch')['CGPA'].mean())