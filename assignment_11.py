square = lambda x: x**2

number = float(input("Enter a number: "))

result = square(number)

print(f"The square of {number} is: {result}")




#Question 2
is_even = lambda x: x % 2 == 0

num_list = input("Enter a list of integers: ").split()
num_list = [int(num) for num in num_list]

even_numbers = list(filter(is_even, num_list))

print("Even numbers from list:", even_numbers)


#Question 3
add_numbers = lambda x, y: x + y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add_numbers(num1,num2)
print(f"The sum of {num1} and {num2} is: {result}")

