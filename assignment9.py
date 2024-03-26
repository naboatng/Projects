# def calculate_average(*args):
#     if not args:
#         return 0
#     total_sum = sum(args)
#     average = total_sum/len(args)

#     # return total_sum instead of returning total_sum you have to return average ok?

#     return average
# #and we also need to call the function like
# # Function calls
# print(calculate_average())  # function call with no argument
# print(calculate_average(4))  # function call with one argument
# print(calculate_average(5, 6))  # function call with two arguments
# print(calculate_average(9, 8, 20))  # function call with three arguments
# print(calculate_average(1, 4, 3, 77, 4, 66, 33, 10, 32, 10))  # function call with ten arguments





# def print_contact_info(first_name, last_name, **kwargs):
#     print("Name:", first_name, last_name)
#     for key,value in kwargs.items():
#         print(f"{key.capitalize()}: {value}")


# print_contact_info("Luke","Shaw", email = "luke_shaw@gmail.com",phone = "718-203-9940")



#Invalid Code
# def find_maximum(*args):
#     if not args:
#         return None
    
#     total_sum = sum(args)
#     largest_number = total_sum/max(args)
#     return total_sum


#Valid Code

def find_maximum(*args):
    if not args:
        return None
    
    largest_number = max(args)
    return largest_number

print("Largest number is:", find_maximum(4, 5, 33, 22, 67, 876))



