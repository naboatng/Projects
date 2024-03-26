import pandas as pd

 
# df = pd.read_csv(r'/Users/nana/Downloads/TopSellingAlbums.csv') 
df = pd.read_csv('TopSellingAlbums.csv') 
print(df)
pd.set_option('display.max_columns',None)

# Question 1
q = df['Rating']
print(q)

#Question 2
q = df.loc['Released','Artist']
print(q)

#Question 3
access = df.iloc[1,2]
print(access)

new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
print(df_new.loc['a', 'Artist'])
print(df_new.loc['a':'d', 'Artist'])
