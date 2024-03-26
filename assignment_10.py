def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

prompt = int(input("Enter a positive integer:"))


print("factorial","is", factorial(prompt))    


#Question 2
# def fibonacci(n):
#     if n < 0 :
#         print("incorrect number")
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) 
# print(fibonacci(10))   


#Correct Code according to your solution but requirements were something else
def fibonacci(n):
    if n < 0:
        print("incorrect number")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


# #Q.2 Corrected
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# User input for n
n = int(input("Enter the value of 'n': "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = fibonacci(n)
    print(f"The {n}th number in the Fibonacci series is: {result}")





#Question 3
# def TrailingZeroes(n):
#     if(n<1):
#         return

#     count = 0
#     for i in range(1,n+1):

#         while i % 5 == 0:
#             count += 1
#             i//=5
#             return count
# n = int(input("Enter positive integer:"))
# print("The factorial of", n, "is", TrailingZeroes, "trailing number")    

'''
 there is a small logical error in the code. The return count statement is placed inside the loop, which causes the function to return the count after processing the first multiple of 5, without checking for other multiples. Additionally, there is an issue with the print statement at the end.
'''

#Q.3 Corrected Code

def TrailingZeroes(n):
    if n < 1:
        return 0  # If n is less than 1, return 0 since there are no trailing zeroes.

    count = 0  # Initialize the count of trailing zeroes.

    for i in range(1, n + 1):
        while i % 5 == 0:
            count += 1
            i //= 5

    return count

n = int(input("Enter a positive integer: "))
trailing_zeroes = TrailingZeroes(n)
print(f"The factorial of {n} has {trailing_zeroes} trailing zeroes.")



# #Question 4

# def tribonnaci(n):
#     if (n<1):
#         return
    

# first = 0
# second = 0
# third = 1

# print(first," ", end=" ")
# if (n > 1):
#     print(second, " ", end= " ")
#     if (n<2):
#         print(second, " ", end=" ")

# for i in range(3, n):
#     tmp = first + second + third 
#     first = secondsecond = thirdthird = tmp

#     print(third, " ", end=" ")

# n = 10
# print(tribonnaci(n))


#Corrected Code

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# User input for n
n = int(input("Enter the value of 'n': "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = tribonacci(n)
    print(f"The {n}th number in the Tribonacci series is: {result}")


