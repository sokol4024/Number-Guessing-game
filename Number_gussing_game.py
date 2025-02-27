import random

# Declaring global variables for the game
number = 0
lower_limit = 0
upper_limit = 0

# This function starts the game and asks the user if they are ready to play
# If the user enters anything other than 'yes' or 'no', it will prompt again
# If the user enters 'yes', it will start the game
# If the user enters 'no', it will exit the game
def game():
    print("Are you ready to begin the number guessing game? (yes/no)")
    start = input().strip().lower()
    if start == "yes" or start == "no":
        if start == "yes":
            print("\nWelcome to the Number Guessing Game!\n")
        elif start == "no":
            print("Thank you for your time. Have a great day!\n")
            exit()
    else:
        print("Please enter 'yes' or 'no' only.\n")
        game()
    user_choice()  # Proceed to the next section of the game

# This function redirects the user to different sections of the game like integer, float, or boolean
def user_choice():
    print("You have three options. Please select one:\n a) Integer\n b) Float\n c) Boolean\n")
    choice = input("Enter your choice:\n").strip().lower()
    if choice in ["a", "b", "c"]:
        if choice == "a":
            print("You have selected the Integer version.")
            get_input_int()
            guess_number_int()
        elif choice == "b":
            print("You have selected the Float version.")
            get_input_float()
            guess_number_float()
        elif choice == "c":
            print("You have selected the Boolean version.")
            get_input_boolean()
            guess_number_boolean()
    else:
        print("Invalid selection. Please enter option (a, b, or c) only.\n")
        user_choice()

# This function takes input as upper and lower limit from the user for the integer version of the game
def get_input_int():
    global number, lower_limit, upper_limit
    take_input = input("Would you like to set the number limits? (yes/no):\n").strip().lower()
    if take_input in ["yes", "no"]:
        if take_input == "yes":
            check_int()
        elif take_input == "no":
            lower_limit = 0
            upper_limit = 100
    else:
        print("Invalid input. Please enter 'yes' or 'no'.\n")
        get_input_int()
    number = random.randint(lower_limit, upper_limit)  # Generate a random number within the range
    print(number, "\n")
    print(f"The randomly selected number is within the range [{lower_limit}, {upper_limit}]\n")

# This function takes input as uper and lower limit from the user for the float version of the game
def get_input_float():
    global number, lower_limit, upper_limit
    take_input = input("Would you like to set the number limits? (yes/no):\n").strip().lower()
    if take_input in ["yes", "no"]:
        if take_input == "yes":
            check_float()
        elif take_input == "no":
            lower_limit = 0
            upper_limit = 1
    else:
        print("Invalid input. Please enter 'yes' or 'no'.\n")
        get_input_float()
    number = round(random.uniform(lower_limit, upper_limit), 2)  # Generate a random float number within the range
    print(number,"\n")
    print(f"The randomly selected number is within the range [{lower_limit}, {upper_limit}]\n")

# This function generates a random boolean value
def get_input_boolean():
    global number
    number = random.choice([True, False])
    print(number,"\n")

# This function checks if the user guessed the correct number for the integer version of the game
def guess_number_int():
    global number
    attempts = 0
    while True:
        try:
            while True:
                try:
                    guess = int(input("Please enter your guess:\n"))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.\n")
                    continue
            attempts += 1
            if lower_limit <= guess <= upper_limit:
                if guess == number:
                    print(f"Congratulationyess! You guessed the correct number in {attempts} attempts.\n")
                    exit_not()
                elif guess < number:
                    print("Your guess is lower than actual number. Try again.\n")
                elif guess > number:
                    print("Your guess is higher than actual number. Try again.\n")
            else:
                print(f"Please enter a number within the range [{lower_limit}, {upper_limit}].\n")
        except ValueError:
            print("Invalid input. Please enter an integer.\n")

# This function checks if the user guessed the correct number for the float version of the game
def guess_number_float():
    global number
    attempts = 0
    while True:
        try:
            while True:
                try:
                    guess = float(input("Please enter your guess:\n"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a float.\n")
                    continue
            attempts += 1
            if lower_limit <= guess <= upper_limit:
                if guess == number:
                    print(f"Congratulations! You guessed the correct number in {attempts} attempts.\n")
                    exit_not()
                elif guess < number:
                    print("Your guess is lower than actual number. Try again.\n")
                elif guess > number:
                    print("Your guess is higher than actual number. Try again.\n")
            else:
                print(f"Please enter a number within the range [{lower_limit}, {upper_limit}].\n")
        except ValueError:
            print("Invalid input. Please enter a float.\n")

# This function checks if the user guessed the correct boolean value
def guess_number_boolean():
    global number
    attempts = 0
    while True:
        while True:
            try:
                guess = str(input("Please enter your guess (True/False):\n")).strip().lower()
                if guess not in ["true", "false"]:
                    print("Invalid input. Please enter 'True' or 'False'.\n")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter 'True' or 'False'.\n")
                continue
        attempts += 1
        if guess == str(number).lower():
            print(f"Congratulations! You guessed the correct value in {attempts} attempts.\n")
            exit_not()
        else:
            print("Incorrect guess. A new random boolean value is generated.\n")
            get_input_boolean()

# This function asks the user if they want to play again
def exit_not():
    global number
    print("Would you like to play again? (yes/no)")
    decision = input().strip().lower()
    if decision in ["yes", "no"]:
        if decision == "yes":
            game_choice()
        elif decision == "no":
            print("Thank you for playing. Goodbye!\n")
            exit()
    else:
        print("Please enter 'yes' or 'no' only.\n")
        exit_not()

# This function asks the user if they want to play the same game or try a different version
def game_choice():
    global number
    print("\nDo you want to continue with the same version or try a different one?\n a) Same version\n b) Different version\n")
    choice = input().strip().lower()
    if choice in ["a", "b"]:
        if choice == "a":
            last_game = type(number)
            if last_game == int:
                get_input_int()
                guess_number_int()
            elif last_game == float:
                get_input_float()
                guess_number_float()
            elif last_game == bool:
                get_input_boolean()
                guess_number_boolean()
            else:
                print("An error occurred. Please try again.\n")
                game_choice()
        elif choice == "b":
            user_choice()
    else:
        print("Please enter options (a or b) only.\n")
        game_choice()


# Check if the input value is an integer
def check_int():
    global lower_limit, upper_limit
    while True:
        try:
            lower_limit = int(input("Please enter the lower limit:\n"))
            upper_limit = int(input("Please enter the upper limit:\n"))

            if lower_limit == upper_limit:
                print("Upper limit and lower limit cannot be the same. Please enter again.\n")
                continue
            elif upper_limit - lower_limit <= 10:
                print("The difference between upper and lower limit must be greater than 10. Please enter again.\n")
                continue

            break  # Exit the loop if both inputs are valid integers
        except ValueError:
            print("Invalid input. Please enter integers only.\n")

    print(f"Lower limit: {lower_limit}, Upper limit: {upper_limit}")


# Check if the input value is an float
def check_float():
    global lower_limit, upper_limit
    while True:
        try:
            lower_limit = float(input("Please enter the lower limit:\n"))
            upper_limit = float(input("Please enter the upper limit:\n"))

            if lower_limit == upper_limit:
                print("Upper limit and lower limit cannot be the same. Please enter again.\n")
                continue
            elif upper_limit - lower_limit <= 1:
                print("The difference between upper and lower limit must be greater than 1. Please enter again.\n")
                continue

            break  # Exit the loop if both inputs are valid integers
        except ValueError:
            print("Invalid input. Please enter flooting values only.\n")

    print(f"Lower limit: {lower_limit}, Upper limit: {upper_limit}")


game()  # Start the game
   