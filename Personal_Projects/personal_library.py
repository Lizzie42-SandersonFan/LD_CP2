# LD 1st Personal Library Program
import time

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
        nonlocal library

        if not library:
            print("You don't have anything in you library to remove! Try a different action.")
            return
        while True:
            title = input("Title of Book: \n").strip().title()
            author = input("Author of Book: \n").strip().title()
            book = f"'{title}' by {author}"
            remove = input(f"Is this the book you want to remove? \n{book} (Y/N)\n").strip().upper()
            if remove == "Y":
                if book in library:
                    library.remove(book)
                    print(f"You removed {book}")
                    break
                else:
                    print(f"Could not find {book} in your library. Check your spelling and try again.")
                    continue
            elif remove == "N":
                while True:
                    again = input("Do you want to try removing AGAIN or LEAVE? (type the uppercase action you want to do)").strip().upper()
                    if again == "AGAIN":
                        break
                    elif again == "LEAVE":
                        break
                    else:
                        print("That seems to be an invalid input. Try again.")
                        continue
                # Left the loop for doing remove again, no to see if they left or are staying
                if again == "AGAIN":
                    continue
                elif again == "LEAVE":
                    break
                else:
                    print("What in world did you do?!?!?!")
            else:
                print("That seems to be an invalid input. Try again.")
                continue

    # View: print the list, NICELY
    def viewLibrary():
        nonlocal library

        if not library:
            print("You don't have anything in you library to view! Try a different action.")
            return
        print("This is your current catalog:")
        for item in library:
            print(item)

    # Search for something: ask user for a word to search by. Look through list and find all instances with that word. Print each item with that word
    def searchLibrary():
        nonlocal library

        if not library:
            print("You don't have anything in you library to search for! Try a different action.")
            return
        while True:
            search = input("What would you like to search for?").strip().title()
            print(f"Items containing '{search}':")
            for item in library:
                if search in item:
                    print(item)
            again = input("Would you like to do another search? (Y/N)").strip().upper()
            if again == "Y":
                continue
            else:
                break
    
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
        choice = input("Enter the number corresponding to what you want to do.\n").strip().upper()
        if choice == "1":
            addItem()
        elif choice == "2":
            removeItem()
        elif choice == "3":
            viewLibrary()
        elif choice == "4":
            searchLibrary()
        elif choice == "5":
            print("Hope you were able to build an amazing catalog of books!")
            break
        else:
            print("That doesn't seem to be a valid input; please try again.")
            continue

personalLibrary()