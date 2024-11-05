def check_age():
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age > 120:
            print("The age entered is not valid. Please enter a realistic age between 0 and 120.")
        else : 
            if age % 2 == 0:
                print("The age " , age , " is even.")
            else:
                print("The age " , age , " is odd.")
    
    except ValueError:
        print("Invalid input. Please enter a numerical value for age.")

check_age()
