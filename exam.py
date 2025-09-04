# Number  1
#  basic calculator with continuous use

def add_num(num1, num2):
    return (num1 + num2)

def subtract_num(num1, num2):
    return (num1 - num2)

def multiply_num(num1, num2):
    return(num1 * num2)

def divide_num(num1, num2):
    if num2 ==0:
        print("Error: cannot divide by zero")
    else:
        return (num1 / num2)
    

while True:
    try:
        print("======Basic calculator use======\n Calculator menu ")
        print("Option:")
        print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n5. Exit")
        
       
        number =input("Choose a number: ")

        num1 = input("Enter your first number")
        num2 = input("Enter your second number")

    

        if number == "1":
            
            print(f"Result:", add_num( num1, num2))
        elif number == "2":
            
            print(f"Result:", subtract_num (num1, num2))
        elif number == "3": 
            print(f"Result:", multiply_num (num1, num2))
         
        elif number == "4":
            
            if num2 ==0:
                print("Error: cannot divide by zero")
            else:
                 print(f"Result:", divide_num(num1, num2))
        elif number == "5":
            print("Exiting the calculator... Goodbye!")
            break
        else: 
            print("Try again later")
    except Exception as e:
        print



# Number 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(input("Enter a number"))
    
    if num % 2 == 0:
        print("The number is an even number")
    else:
        print("Goodbye!")


# Number 3
while True:
        age = input("Enter your age (or type exit to quit): ")
        if age == exit:
            print("Goodbye!")
            break
        
        try:
            if age >= 18:
                print("You can vote")
            else:
                print("You cannot vote")
        except:
            print("Invalid input")
        
