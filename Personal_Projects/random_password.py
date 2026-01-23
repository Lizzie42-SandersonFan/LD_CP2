# LD 1st Random Passowrd Generator
import secrets
import time
delay = 0.06

# OVERVIEW
# Create a program that allows a user to specify password requirements (length, upper/lowercase letters, numbers, and special characters) then gives them 4 possible passwords they could use. 

# STEPS
# A main function that runs the code
# Functions for the different password requirements
# A function that assembles that password once it is the correct length
# Users should be able to specify length and if they want to include
    # uppercase letters
    # lowercase letters
    # numbers
    # special characters
 
# Main Func: Build inner functions, greet user, ask user for password paramiters. Use inner functions to build four different passwords. Show user the four different passwords
def random_password():
    # func for length. Ask user how long it needs to be. return length
    def pass_length():
        while True:
            length = input("How long would you like your password to be (Whole number)?\n").strip().upper()
            if length.isdigit() == True:
                if float(length) <= 4.0:
                    print("Password can not be that short. Try again")
                    continue
                else:
                    if int(length) % 1 == 0:
                        # User gave a valid number
                        break
                    else:
                        print("You seemed to have entered a number, but it's not a whole number. Try again")
                        continue
            else:
                print("You seem to have entered something other than a number. Try again")
                continue
        return int(length)
    
    # func for getting parameters. Return Y or N
    def parameter(para):
        while True:
            included = input(f"Would you like {para} in your password? (Y/N)\n").strip().upper()
            if included == "Y":
                print(f"The program will include {para} in your password\n")
                break
            elif included == "N":
                print(f"The program will not include {para} in your password\n")
                break
            else:
                print("You seem to have entered something other than Y or N. Try again")
                continue
        return included

    # func for assembly. The secrets library. Picks a random item without it being known
    # I was having a problem with the passwords being too long. It corresponded to the number of times there was a "Y" (weird math thing. I know why, but can't deal with it in a reasonable short way). To fix this, I truncated the string to the requested length.
    def assemble():
        the_length = pass_length()
        upper_yes = parameter("uppercase letters")
        lower_yes = parameter("lowercase letters")
        num_yes = parameter("numbers")
        special_char_yes = parameter("special characters")
        num = 1
        
        while num <= 4:
            password_list = []
            for _ in range(the_length):
                if upper_yes == "Y":
                    password_list.append(secrets.choice(upper_letters))
                if lower_yes == "Y":
                    password_list.append(secrets.choice(lower_letters))
                if num_yes == "Y":
                    password_list.append(secrets.choice(numbers))
                if special_char_yes == "Y":
                    password_list.append(secrets.choice(special_chars))
            # Make list into string so it can be shortened
            password = "".join(password_list)
            shortened_password = password[:the_length]
            # With how characters are added, I want to make sure that everything the user requested is in there and those requests end up at the front. Can't be randomized yet so that I know at least one request ends up in there
            # Make shortened string back into list so that it can be randomized now
            shortened_password = list(shortened_password)
            secrets.SystemRandom().shuffle(shortened_password)
            # Turn shortened AND randomized list back into a string to be printed
            final_password = "".join(shortened_password)
            print(f"Password {num}: {final_password}")
            num += 1
        

    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', "<", ">", ",", ".", "?", "/"]

    greet = "Welcome user!\nThis program will generate four random passwords for you to use based on parameters YOU choose!\nLet's get started!\n"
    for char in greet:
        print(char, end="", flush = True)
        time.sleep(delay)
    
    while True:
        action = input("Type the number for what you would like to do:\n1. Generate Random Passwords\n2. Leave Program\n")
        if action == "1":
            assemble()
        elif action == "2":
            print("Thank you for using the program! Good bye!")
            break
        else:
            print("Invalid input. Try again")
            continue

random_password()