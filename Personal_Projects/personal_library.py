# LD 1st Personal Library Program
import time

# OVERVIEW
# Create a program that allows user to manage a personal library catalog for any ONE type (books, movies, music, etc). The project needs to allow users to add new items, display ALL contents, search for a specific item (by title, author/artist/director), remove a book from the library, exit the program. 

# STEPS
# Stores all items in a list
# Function to add a new item
# Function to search the items
# Function to remove an item
# Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
# Project must include
    # easy to understand variable and function names
    # Pseudocode comments explaining what the code is doing
    # Good use of white space to keep items separate and easy to read/find


# FUNCTIONS

# Run game: First build all iner functions. Then establish the list of books. Have a while loop running the program with the option to add, view, remove, search, and leave
def personalLibrary():

    # Add items: First, ask the user for book title. Then ask user for author. Combine thoes two into one item. Append that combined item. Done
    def addItem():
        nonlocal library

        title = input("Title of Book: \n").strip().title()
        author = input("Author of Book: \n").strip().title()
        book = f"'{title}' by {author}"
        print(f"You added the book {book}")
        library.append(book)

    # Remove Items: Ask user for book title and author. look in list for item. Ask user if this is the item they want to remove. if yes, remove it from list. If no, either restart removing process or ask user if they want to go back to main menu
    def removeItem():
        pass


    # View: print the list, NICELY
    def viewLibrary():
        nonlocal library
        print("This is your current catalog:")
        for item in library:
            print(item)

    # Search for something: ask user for a word to search by. Look through list and find all instances with that word. Print each item with that word
    def searchLibrary():
        pass

    library = []
    delay = 0.04

    greet = "\nWelcome! In this program, you will be able to catalog all of your books in your very own personal library!\n"
    for char in greet:
        print(char, end="", flush = True)
        time.sleep(delay)

    while True:
        time.sleep(.5)
        show = "What would you like to do?\n(1) Add Book\n(2) Remove Book\n(3) View Catalog\n(4) Search Catalog\n(5) Leave\n"
        for char in show:
            print(char, end="", flush = True)
            time.sleep(delay)
        choice = input("Enter the number corresponding to what yyou want to do.\n").strip().upper()
        if choice == "1":
            addItem()
        elif choice == "2":
            removeItem()
        elif choice == "3":
            viewLibrary()
        elif choice == "4":
            searchLibrary()
        elif choice == "5":
            print("How you were able to build an amazing catalog of books!")
            break
        else:
            print("That doesn't seem to be a valid input; please try again.")
            continue

personalLibrary()