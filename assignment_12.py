##Your solution was correct but we have to utilize the user input too
# global_var = 10

# def modification_var(value):
#     prompt= int(input("Enter a value:"))
#     modi_var = value+prompt
#     return modi_var

# results = modification_var(global_var)
# print("The variable before",global_var)
# print("The variable after",results)





#Question 2
# global_var = 10

# def scoping_rule():
#     global_var = 5 # Local variable with the same name as the global variable
#     print("The inner global variable",global_var) 
  
# print("Global variable before taking user input: ",global_var)

# # Prompt the user to enter a value for the global variable

# global_var = int(input("Enter a value for the global variable: "))

# #now global varibal is updated 
# print("The outter global variable is ",global_var)
# #function call
# scoping_rule()

# print("Global variable after the function call:", global_var)




#Question#3 
#Invalid Code 
# def outer(value):
#     outer_var = value+6
#     return outer_var

#     prompt = int(input("Enter a number: "))
#     def inner(value):
#         print("The before modification:",inner)

#     modify = inner(value)
#     print("The after modufication:",modify)



# Valid Code

# def outer(value):
#     outer_var = value + 6

#     def inner():
#         nonlocal outer_var
#         print("Before modification (inner function):", outer_var)
#         outer_var += 10
#         print("After modification (inner function):", outer_var)

#     inner()  # Call the inner function to modify the nonlocal variable
#     return outer_var

# prompt = int(input("Enter a number: "))
# result = outer(prompt)
# print("The final value (outer function):", result)




#Question #4
#invalid code
# def myfunction():
#         global blue 
#         prompt = input("What the color of the car:")
# myfunction()
# print("My favorite color is",prompt)




# Valid code
blue = ''  # Declare the global variable outside the function

def myfunction():
    # Use the global variable without explicitly declaring it as global
    # However, we need to use 'global' if we want to modify the global variable inside the function
    global blue
    blue = input("What is the color of the car: ")

myfunction()
print("My favorite color is", blue)
