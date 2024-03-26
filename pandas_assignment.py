import pandas as pd

# Problem 1
z = {'Student':['David','Samuel','Terry','Evan'],'Age':[27,24,22,32],
     'Country':['UK','Canada','China','USA'], 
     'Courses':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':[85,72,89,76]}
df = pd.DataFrame(z)
print(df)

# Problem 2:
#Retrieved the Mark column and assign to b
b = df[['Marks']]
print(b)

#Problem 3
c = df[['Country','Courses']]
print(c)



