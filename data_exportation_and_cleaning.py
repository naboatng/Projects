import pandas as pd
import numpy as np

# Exercise 1
my_data = {'Name': ['Eve', 'Frank', 'Grace'], 'Age': [28, 22, 30]}
df = pd.DataFrame(my_data)
df.to_csv('my_data.csv', index=False)

# Exercise 2
data = {'Country': ['USA', 'Canada', 'Mexico'],
        'Population(millions)': [328, 37, 126]}
df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False, sheet_name='Sheet1')

# Exercise 3
population = {'Country': ['USA', 'Canada', 'Mexico'],
              'Population (millions)': [328, 37, 126]}  # Renamed the column for consistency
df = pd.DataFrame(population)
df.to_excel('population.xlsx', index=False, sheet_name='CountryData')

# Exercise 4
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 12, 13, np.nan, 15]}
df = pd.DataFrame(data)
df.dropna(inplace=True)

# Exercise 5
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25]}
df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)  # Added inplace=True to modify the DataFrame in place

# Exercise 6
data = {'Category': ['A', 'B', 'C'],
        'Value': ['1.2', '3.4', '5.6']}
df = pd.DataFrame(data)
df['Value'] = df['Value'].astype(float)

# Display the DataFrames if needed
print(df)  # You can print the DataFrames to check the results
