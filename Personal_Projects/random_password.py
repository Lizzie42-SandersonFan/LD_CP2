# LD 1st Random Passowrd Generator
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
# HINT: You can make this by randomly selecting from different lists OR by randomly generating the ASCII letters! 
 
# Main Func: Build inner functions, greet user, ask user for password paramiters. Use inner functions to build four different passwords. Show user the four different passwords
def random_password():
    # func for length. Ask user how long it needs to be. return length
    def pass_length():
        while True:
            length = input("How long would you like your password to be (Whole number)?\n").strip().upper()
            if length.isdigit() == True:
                if int(length) == True:
                    # User gave a valid number
                    break
                else:
                    print("You seemed to have entered a number, but it's not a whole number. Try again")
                    continue
            else:
                print("You seem to have entered something other than a number. Try again")
                continue
        return int(length)
    
    # func for uppercase needed. Yes/No. return yes/no
    def pass_upper():
        while True:
            upper = input("Would you like uppercase in your password (Y/N)\n").strip().upper()
            if upper == "Y":
                print("Uppercase will be included in your password")
                break
            elif upper == "N":
                print("Uppercase will not be included in your password")
                break
            else:
                print("You seem to have entered something other than Y or N. Try again")
                continue
        return upper
    
    # func for lowercase needed. Yes/No. return yes/no
    def pass_lower():
        while True:
            lower = input("Would you like lowercase in your password (Y/N)\n").strip().upper()
            if lower == "Y":
                print("Lowercase will be included in your password")
                break
            elif lower == "N":
                print("Lowercase will not be included in your password")
                break
            else:
                print("You seem to have entered something other than Y or N. Try again")
                continue
        return lower
    
    # func for numbers needed. Yes/No. return yes/no
    def pass_number():
        while True:
            number = input("Would you like numbers in your password (Y/N)\n").strip().upper()
            if number == "Y":
                print("Numbers will be included in your password")
                break
            elif number == "N":
                print("Numbers will not be included in your password")
                break
            else:
                print("You seem to have entered something other than Y or N. Try again")
                continue
        return number
    
    # func for special characters needed. Yes/No. return yes/no
    def pass_special_char():
        while True:
            special_char = input("Would you like special characters in your password (Y/N)\n").strip().upper()
            if special_char == "Y":
                print("Special characters will be included in your password")
                break
            elif special_char == "N":
                print("Special characters will not be included in your password")
                break
            else:
                print("You seem to have entered something other than Y or N. Try again")
                continue
        return special_char

    # func for assembly. I need to figure this out
    def assemble():
        pass_length()
        pass_upper()
        pass_lower()
        pass_number()
        pass_special_char() 
        # How doth one do this?
        # I know I need to use the parameters from the functions to determine what to pull from all the lists, but how do I know how many from each? Maybe random numbers?

    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    special_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', "<", ">", ",", ".", "?", "/"]

    greet = "Welcome user! This program will generate four random passwords for you to use based on parameters YOU choose! Let's get started!"
    for char in greet:
        print(char, end="", flush = True)
        time.sleep(delay)
    
    while True:
        action = input("Type the number for what you would like to do:\n1. Generate Random Passwords\n2. Leave Program")
        if action == "1":
            assemble()
        elif action == "2":
            print("Thank you for using the program! Good-bye!")
            break
        else:
            pass