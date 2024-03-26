# a = ["0", 1, "two", "3", 4]
# print("a[0]:", a[0])
# print("a[1]:", a[1])
# print("a[2]:", a[2])
# print("a[3]:", a[3])
# print("a[4]:", a[4])

# type(a)


import numpy as np
# a = np.array([0,1,2,3,4])
# for i in a:
#     print(i)

# print(np.__version__)   



b = np.array([3.1, 11.02, 6.2, 21.3, 5.2])
# Check the type of the array
print(type(b))
c = b.shape
print(c)
print(b.dtype)





a = np.array([10, 2, 30, 40, 50])
a[1] = 20
print(a)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.arange(2,9,2))

b = np.array([10,20,30,40,50,60,70])
print(b.ndim)
print(b.size)
print(b.shape)

arr = np.array([-5,-3,-2,0,1,2,3,4,5,])
max_arr = arr.max()
print(max_arr)

min_arr = arr.min()
print(min_arr)

total_sum = max_arr+min_arr

print("=====", total_sum)