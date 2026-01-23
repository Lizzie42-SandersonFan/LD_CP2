# LD 2nd Simple Morse Code Translator

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
letters = {
    "A": " .- ",
    "B": " -... ",
    "C": " -.-. ",
    "D": " -.. ",
    "E": " . ",
    "F": " ..-. ",
    "G": " --. ",
    "H": " .... ",
    "I": " .. ",
    "J": " .--- ",
    "K": " -.- ",
    "L": " .-.. ",
    "M": " -- ",
    "N": " -. ",
    "O": " --- ",
    "P": " .--. ",
    "Q": " --.- ",
    "R": " .-. ",
    "S": " ... ",
    "T": " - ",
    "U": " ..- ",
    "V": " ...- ",
    "W": " .-- ",
    "X": " -..- ",
    "Y": " -.-- ",
    "Z": " --.. ",
    "1": " .---- ",
    "2": " ..--- ",
    "3": " ...-- ",
    "4": " ....- ",
    "5": " ..... ",
    "6": " -.... ",
    "7": " --... ",
    "8": " ---.. ",
    "9": " ----. ",
    "0": " ----- ",
}

# Main run loop. Greet, ask user what they would like to do
while True:
    pass

# IDEAS:
# Could I use a turn a string into a list? Then with the morse code, each item in the list is determined if there is a space at the end