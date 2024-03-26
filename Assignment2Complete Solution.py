print(" ")
print("Select an option:")
print(" ")

print("1. Check if number is even or odd:")
print("2. Print all even numbers from 1 to:")
print("3. Multiplication from 1 to 10: ")
print("0. Exit program. ")
print(" ")


while True:
    option = int(input("Enter a number to select an option: ")) # always use a reasonable variable name
    print(" ")
    
    if option == 1:

        print(" ")
        number = int(input("Please enter a number to check even or odd:"))
        if number % 2==0:
            print(number," is an even number")
        elif number % 2!=0:
            print(number," is an odd number")
        else:
            print("Please Enter A Valid Number")
        continue

    elif option == 2:
        print(" ")
        newNumber = int(input("Please enter a limit number to print all even numbers: "))
        for i in range(1,newNumber+1):
            if i % 2 ==0:
                print(i)
            else:
                continue

    elif option == 3:
        print(" ")

        multiple = int(input("Enter an integer: "))

        for count in range(1,11) :
            product = multiple * count
            print(multiple, "x", count, "=",product)
            continue


    elif option == 0:
        break

    else:
        print("Please enter a valid number!")  
        continue




