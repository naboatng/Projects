print("-- Loop and Conditional Statement Program --")

def maninMenu():
    print()
    print("Select an option")
    print()
    print("Menu:")
    print("1. Check if a number is even or odd")
    print("2. Print even numbers up to limit to a limit ")
    print("3. Calculate sum of positive and absolute sum of negative numbers")
    print("4. Multiplication table")
    print("5. Exit")
    print()

    while True:
        option = int(input("Enter your selection(1/2/3/4/5): "))
        if option == 1:
            user_input = int(input("Enter a number to check if its even or odd :" ))
            if user_input % 2 == 0:
                print(user_input,"Its an even number")   
            else:
                print(user_input,"Its an Odd number ")
                continue  

        elif option == 2:
            limit = int(input("Enter the limit to print even numbers: "))
            for i in range(1,limit+1):
                if i % 2 == 0:
                    print(i)          
            

        elif option == 3:
            arr = []
            positive = 0
            negative = 0

            series = int(input("Enter a series of numbers (enter '0' to stop):"))
            while True:
                
                x = int(input("Enter a number  :"))
                if x == 0:
                    break
                arr.append(x)
                if x > 0:
                    positive +=x   
                else:
                     negative +=x
            print("The sum of all positive numbers:",positive)  
            print("The sum of all negative numbers:",negative) 
            
            


        elif option == 4:
            num = int(input("Enter a number to print its multiplication table: "))
            for i in range(1,10):
                #print("Multiplication table of :",num)
                print(num,"*",i,"=",num * i)
                continue
        elif option == 5:
            print("Exiting the program. Goodbye!")
            break

maninMenu()        
