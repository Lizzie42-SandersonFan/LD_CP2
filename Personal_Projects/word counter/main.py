# LD 1st Main File for Word Counter
from helpers import *
from file_handle import *
from time_handle import *

# Main menu shows the options to 1) Give file path 2) View file 3) add to file 4) Leave (This will show the word count before they leave)

def main():
    have_path = False
    type_print("Welcome user! This program will let you type on a document and at they end, show you how many words you have in your document.\n")
    while True:
        type_print("What would you like to do:\n1) Give File Path\n2) View File\n3) Add to File\n4) Leave\n")
        choice = input("Type the number corresponding to what you want to do:\n")
        if choice == "1":
            the_path = get_file_path()
            have_path = True
        elif choice == "2":
            if have_path == True:
                read_file(the_path)
            else:
                print("You have not given a path for your file.\nPlease give a path before continuing")
                continue
        elif choice == "3":
            if have_path == True:
                add_to_file(the_path)
            else:
                print("You have not given a path for your file.\nPlease give a path before continuing")
                continue
        elif choice == "4":
            word_count = get_word_count(the_path)
            print(f"Thank you for using the program! Word count of document: {word_count}")
            break
        else:
            print("Invalid input. Try again")
            continue
main()