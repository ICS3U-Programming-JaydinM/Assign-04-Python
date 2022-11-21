#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-11-16
# This program tells the user the factors of the number the user has inputted 
# It makes sure the number is a integer and is positive 


def main ():


    # Tries to get the user_number as a positive integer.
    try:
        user_number = int(input("Enter a positive integer that you would like to factor:"))
        print()
    # If the user does not enter a number
    except ValueError:
        print("You need to enter a positive integer.")
        main()
    # If the user enters a negative number it Restarts the program
    if user_number < 0:
        print("You need to enter a positive integer.")
        main()
    #give num a value
    num = int(user_number)
    
    print("\nFactors of " +str(user_number)+ " are ")
    #It's the calculator of the program for use number
    for counter in range(1, num+1):
        # % means it returns the remainder of dividing the left hand operand by right hand operand
        if num % counter == 0:
            print(str(counter))
    print()
    
if __name__ == "__main__":
    main()
    print("Thanks For Playing!")
    print()
    print()

    # asks the user if they want to restart after the program has finished
    restart = int(input("Enter 1 if you'd like to restart: "))
    while restart == 1:
        main()
        restart = int(input("Enter 1 if you'd like to restart: "))