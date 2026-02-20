# LD 1st Main File for Word Counter
from helpers import *
from file_handle import *

# Main menu shows the options to 1) Give file path 2) View file 3) add to file 4) Leave (This will show the word count before they leave)

def main():
    type_print("Welcome user! This program will let you type on a document and at they end, show you how many words you have in your document.")
    while True:
        type_print("What would you like to do:\n1) Give File Path\n2) View File\n3) Add to File\n4) Leave\n")
        choice = input("Type the number corresponding to what you want to do:\n")
        if choice == "1":
            the_path = get_file_path()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Invalid input. Try again")
            continue