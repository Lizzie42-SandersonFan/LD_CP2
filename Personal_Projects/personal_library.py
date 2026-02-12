# LD 1st Personal Library Program
import time
import csv
# import pandas

# RELOGIC THINGS. Current run has a list that AT THE END is added to the csv. Fix stuff
# FUNCTIONS

# Run game: First build all iner functions. Then establish the list of books. Have a while loop running the program with the option to add, view, remove, search, and leave
def personalLibrary():
    # Function that will check if there is anything in the csv. That way, nothing crashes if the user tries to edit the library with nothing in it
    def csv_has_stuff(path):
        try:
            with open(path, "r") as file:
                try:
                    content = file.read()
                    headers = next(content)
                    return True
                except StopIteration:
                    return False
        except:
            print("There was a problem reading the file. Do not know if there is stuff in the file")
    # Add items: First, ask the user for book title. Then ask user for author. Combine thoes two into one item. Append that combined item. Done
    def addItem():
        title = input("Title of Book: \n").strip().title()
        author = input("Author of Book: \n").strip().title()
        while True:
            year = input("What year was this book published:\n").strip().lower()
            if int(year) == False and len(year) != 4:
                print("Invalid year. Please try again")
                continue
            else:
                break
        genre = input("What is the genre for this book:\n").strip().title()
        try:
            with open("Personal_Projects/the_personal_libraray.csv", "a", newline="") as csvfile:
                fieldnames = ['title', 'author', 'publish year', 'genre']
                writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                writer.writerow({'title': title, 'author': author, 'publish year': year, 'genre': genre})
        except:
            print("Encountered a file issue.\nReturning to main menu to try again")
        print(f"You added the book: '{title}' by {author}")

    # Remove Items: Ask user for book title and author. look in list for item. Ask user if this is the item they want to remove. if yes, remove it from list. If no, either restart removing process or ask user if they want to go back to main menu
    def removeItem():
        if csv_has_stuff("Personal_Projects/the_personal_libraray.csv") == False:
            print("You don't have a libaray to edit! Try adding something before removing.")
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

    # View: show either simple (Title + author) or detailed (everything)
    def viewLibrary():
        if csv_has_stuff("Personal_Projects/the_personal_libraray.csv") == False:
            print("You don't have a libaray to edit! Try adding something before removing.")
            return
        print("This is your current catalog:")
        for item in library:
            print(item)

    # Search for something: ask user for a word to search by. Look through list and find all instances with that word. Print each item with that word
    def searchLibrary():
        if csv_has_stuff("Personal_Projects/the_personal_libraray.csv") == False:
            print("You don't have a libaray to search! Try adding something before removing.")
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
    
    # Function to update item

    # Reload the libary. Current run has a list of things the user wants to add and if this is called, clear the list and dont add it to the csv
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