#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-11-16
# This program tells the user the factors of the number the user has inputted
# It makes sure the number is a integer and is positive


from termcolor import colored


# Defining the color selection function
def color_selection():

    # Displays the colors
    print("COLOR MENU")
    colors = ["Red", "Blue", "white", ]
    number = 0
    for i in colors:
        number += 1
        print(f"{number}. {i}")

    # Get's the user's color choice
    user_color = input("\33[3mChoose a color from the list : ")

    # Tries casting user_color to an integer
    try:
        user_color = int(user_color)

    # Restarts the function after a key is entered
    except ValueError:
        print("\33[3mYou must enter a positive integer.")
        color_selection()
    # Makes color variable available to main function
    global color

    # Match-case structure for color choices
    match user_color:
        case 1:
            color = "red"
        case 2:
            color = "blue"
        case 3: 
            color = "white"

def main():
    color_selection()
    user_number = input(colored("\33[3mEnter a positive integer that you would like to factor:", color))
    # Tries to get the user_number as a positive integer.
    try:
        user_number = int(user_number)
        print()
    # If the user does not enter a number
    except ValueError:
        print("\33[3mYou need to enter a positive integer.")
        main()
    # If the user enters a negative number it Restarts the program
    if user_number < 0:
        print("\33[3mYou need to enter a positive integer.")
        main()
    # give num a value
    num = int(user_number)

    print(colored("\33[3m\nFactors of " + str(user_number) + " are ", color))
    # It's the calculator of the program for use number
    for counter in range(1, num + 1):
        # % means it returns the remainder of dividing the left hand operand by right hand operand
        if num % counter == 0:
            print (str(counter, ))
    print()


if __name__ == "__main__":
    main()
    print(colored("\33[3mThanks For Playing!", color))
    print()
    print()

    # asks the user if they want to restart after the program has finished
    restart = int(input(colored("\33[3mEnter 1 if you'd like to restart: ", color)))
    while restart == 1:
        main()
        restart = int(input(colored("Enter 1 if you'd like to restart: ", color)))
