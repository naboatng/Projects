import pandas as pd

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4],
'Department': ['Architect Group', 'Software Group', 'Design Team',
'Infrastructure'],
 'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)
print(df)

# Problem 4 

department_jane = df.loc[df['Name'] == 'Jane', 'Department']
print(department_jane)

#Problem 5
df.iloc[3,-4]
mary_salary = df.iloc[3]['Salary']
print(mary_salary)

#Problem 6
jane_info = df.loc[df['Name'] == 'Jane']
print(jane_info)



# Explantion


'''Problem 4: Accessing Jane's Department using .loc

df.loc[df['Name'] == 'Jane', 'Department'] locates the row where the 'Name' column is 'Jane' and then retrieves the 'Department' column value for Jane.
This code correctly finds and prints Jane's department.



Problem 5: Accessing Mary's Salary using .iloc

df.iloc[3]['Salary'] uses integer-based indexing with .iloc to access the fourth row (index 3) and then retrieves the 'Salary' column value for Mary.
This code correctly finds and prints Mary's salary.


Problem 6: Accessing Jane's Information using .loc

df.loc[df['Name'] == 'Jane'] locates the row(s) where the 'Name' column is 'Jane' and retrieves all columns' values for Jane.
This code correctly finds and prints all information about Jane, including her Name, ID, Department, and Salary.
'''