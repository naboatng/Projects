# Assignment Marked, Your markes:


import numpy as np

#Task 2
my_array = np.array([2,4,6,8,10])
print(my_array)

my_array =np.sum([2,8,4,6,10])
print(my_array)

#Task 3
my_array = np.array([2,4,6,8,10])
print(my_array.mean())

my_array = np.array([2,4,6,8,10])
print(my_array.max())

my_array = np.array([2,4,6,8,10])
print(my_array.min())

#Task 4
my_array = np.array([2,4,6,8,10])
# print(my_array[1:4:2]) 

'''
Extract the second and third elements of the array.
print(my_array[1:4:2])

Here, my_array[1:4:2] will actually give you the second and fourth elements of the array, not the second and third.

To extract the second and third elements (4 and 6) of the array, you can use


'''
print(my_array[1:3])

print(my_array[1:4])

#Task 5
multiplier = np.array([2,2,2,2,2])
my_array = np.array([2,4,6,8,10])
result = multiplier * my_array
print(result)

#Task 6
grades = np.array([85, 92, 78, 90, 88])
passing = []
for i in grades:
    if i >= 80:
        #no need to append boolean values in string 
        # you should print these values as it as ok?
        
        passing.append(True)
    else:
        passing.append(False)
   
print(passing)  

#Question 7
#Write a brief summary of what you have learned about 
# working with 1D Numpy arrays
#and how they can be useful in data 
# analysis and scientific computing.

#1D Numpy Arrays allow to work and access from one assign list
#It can help in analysizing a single column of a numpy array.
#You can access and manipulate individual elements or slice of a 1D NumPy array using index and slicing
#notation
#You can filter,transform and reshape data efficiently.