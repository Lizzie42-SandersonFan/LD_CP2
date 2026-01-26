# LD 2nd Simple Morse Code Translator
import time

# OVERVIEW
# Write a program that will translate between English and Morse Code

# REQUIREMENTS
# Create two tuples (one of the alphabet letters in English, and other for the corresponding Morse Code Symbols) 
# Create a function to translate English into Morse Code
# Create a function to translate Morse Code into English
# Create a main loop where users can choose to translate English to Morse Code, Morse Code to English, or Exit
# Project needs to:
    # Use string manipulation to control the appearance of the output 
    # Use basic error handling (for characters not in Morse Code)
    # Use good naming for functions and variables
    # Use pseudocode comments to explain what the program is doing
    # Use white space to make sure code is easy to read


# Function English -> Morse Code
# This will take in a string in english. Then, for each character in the string, find it in the tuple and replace that item in the original string with the morse code. Between each set of dots and dashes, put a space and where there is a space, replace it with two spaces. When translation is done, return the translation


# Function Morse Code -> English
# This will take in a string of dots and dashes. I will know a set of dots and dashes is one character by looking for the space at the end. Take that set of dots and dashes and find it in the tuple, and replace the set of dots and dashes with the english character. Make sure the new english character has no spaces surounding it. If there are two spaces in a row, replace it with a single space.

# VARIABLES
delay = 0.06
english_letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
morse_code = (" .-", " -...", " -.-.", " -..", " .", " ..-.", " --.", " ....", " ..", " .---", " -.-", " .-..", " --", " -.", " ---", " .--.", " --.-", " .-.", " ...", " -", " ..-", " ...-", " .--", " -..-", " -.--", " --..", " .----", " ..---", " ...--", " ....-", " .....", " -....", " --...", " ---..", " ----.", " -----")

# FUNCTIONS
def type_print(string):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

def mc_2_eng():
    translation = []
    # Steps: 
    # 1. ask user for the morse code they need translated
    # 2. convert string to list
    # 3. for each item in the user list, find it in morse_code list. Use that same index to get english letter. Append that retrived item into a new list that is the translation
    # IF that item cannot be found in the list, take that item and just imediatly append it into translation list
    # 4. Once translation list is done, convert it into a string
    # 5. return final translation string
    pass

def eng_2_mc():
    translation = []
    # Steps: 
    # 1. ask user for the english they need translated
    # 2. convert string to list
    # 3. for each item in the user list, find it in english_letters list. Use that same index to get morse code letter. Append that retrived item into a new list that is the translation
    # IF that item cannot be found in the list, take that item and just imediatly append it into translation list
    # 4. Once translation list is done, convert it into a string
    # 5. return final translation string
    pass

# Main run loop. Greet, ask user what they would like to do
def main():
    greet = "Hello user!\nThis program is a morse code translator,\nand will allow you to translate to and from morse code to english!\n"
    type_print(greet)
    while True:
        show_choice = "\nWhat would you like to do:\n1) Translate English to Morse Code\n2) Translate Morse Code to English\n3) Leave\n"
        type_print(show_choice)
        action = input("Enter the number corresponding to what you want to do\n")
        if action == "1":
            eng_2_mc()
        elif action == "2":
            mc_2_eng()
        elif action == "3":
            leave = "Thank you for using this program! Have a nice day!\n"
            type_print(leave)
            break
        else:
            invalid = "It seems you have entered an invalid input. Try again\n"
            type_print(invalid)
            continue

main()
# IDEAS:
# Could I use a turn a string into a list? Then with the morse code, each item in the list is determined if there is a space at the end