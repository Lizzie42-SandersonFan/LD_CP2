# LD 1st Personal Library Program
import time
import csv
# import pandas

# RELOGIC THINGS. Current run has a list that AT THE END is added to the csv. Fix stuff
# FUNCTIONS

# Run game: First build all iner functions. Then establish the list of books. Have a while loop running the program with the option to add, view, remove, search, and leave
def personal_library():
    library = []
    removed_items = []
    def type_print(string, delay = 0.04):
        for char in string:
            print(char, end="", flush = True)
            time.sleep(delay)

    # Function that will check if there is anything in the csv. That way, nothing crashes if the user tries to edit the library with nothing in it
    def csv_has_stuff(path = "Personal_Projects/the_personal_libraray.csv"):
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
    def add_item():
        nonlocal library
        
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
        notes = input("Any notes for this book (if none, put a space)").strip().capitalize()
        library.append({'title': title, 'author': author, 'publish year': year, 'genre': genre, 'notes': notes})
        print(f"You added the book: '{title}' by {author}")

    # Remove Items: Ask user for book title and author. look in list for item. Ask user if this is the item they want to remove. if yes, remove it from list. If no, either restart removing process or ask user if they want to go back to main menu
    def remove_item():
        nonlocal library
        nonlocal removed_items
        if csv_has_stuff("Personal_Projects/the_personal_libraray.csv") == False or not library:
            print("You don't have a libaray to edit! Try adding something before removing.")
            return
        while True:
            while True:
                file_choice = input("Would you like to remove something in the\n1) run library\nor\n2) the saved file").strip().lower()
                if file_choice == "1":
                    break
                elif file_choice == "2":
                    break
                else:
                    print("Invalid input. Try again")
                    continue
            title = input("Title of Book: \n").strip().title()
            author = input("Author of Book:\n").strip().title()
            if file_choice == "1":
                # Removing something from run library
                for item in library:
                    if title in item and author in item:
                        # book meets requirments, ask user if they want to remove it
                        print(f"Found '{item['title']}' by {item['author']}")
                        while True:
                            remove = input(f"Do you wish to remove '{item['title']}' by {item['author']} (Y/N)?\n").strip().upper()
                            if remove == "Y":
                                library.remove(item)
                                return
                            elif remove == "N":
                                again = input("Would you like to\n1) Return to Main Menu\nor\n2) Do Removing Process again")
                                if again == "2":
                                    remove_item()
                                else:
                                    print("Returning to main menu . . .")
                                    return
                            else:
                                print("Invalid input. Try again")
                                continue
                    else:
                        # book does not meet requirements, move to next one
                        pass  
                else:
                    print(f"Could not find any books feturing the title '{title}' and author {author}.")
                    try_again = input("Would you like to try the removal process again (Y/N):\n").strip().upper()
                    if try_again == "Y":
                        update_item()
                    else:
                        print("Returning to main menu . . .")
                        return
            elif file_choice == "2":
                # removing something in csv
                try:
                    with open("Personal_Projects/the_personal_libraray.csv", "r+", newline = '') as csv_file:
                        reader = csv.reader(csv_file)
                        for row in reader:
                            if row['title'] == title and row['author'] == author:
                                while True:
                                    print(f"Found: {row}")
                                    removed = input("Do you wish to remove it (Y/N)?\n").strip().upper()
                                    if removed == "Y":
                                        removed_items.append(row)
                                        return
                                    elif removed == "N":
                                        again2 = input("Would you like to\n1) Return to Main Menu\nor\n2) Do Removing Process again")
                                        if again2 == "2":
                                            remove_item()
                                        else:
                                            print("Returning to main menu . . .")
                                            return
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                except:
                    print("Had trouble reading the file in removeItem func")
            else:
                print("The program could not find a book with the title and author you specified, or the libaray section you wanted to edit didn't have the item.\nTry again and check your spelling")
                continue
        
    # View: show either simple (Title + author) or detailed (everything)
    def view_library(complexity):
        if csv_has_stuff("Personal_Projects/the_personal_libraray.csv") == False:
            print("You don't have a libaray to edit! Try adding something before removing.")
            return
        print("This is your current catalog:")
        if complexity == "simple":
            for item in library:
                print(f"Book: '{item['title']}' by {item['author']}\n")
            try:
                with open("Personal_Projects/the_personal_libraray.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    for line in content:
                        print(f"Book: '{line[0]}' by {line[1]}\n")
            except:
                print("There was a problem with reading the file in viewing")  
        elif complexity == "detailed":
            for item in library:
                print(f"Title: {item['title']}\nAuthor: {item['author']}\nPublish in {item["publish year"]}\nGenre: {item['genre']}\nNotes for this Book: {item['notes']}")
            try:
                with open("Personal_Projects/the_personal_libraray.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    for line in content:
                        print(f"Title: {line[0]}\nAuthor: {line[1]}\nPublished in: {line[2]}\nGenre: {line[3]}\nNotes for this Book: {line[4]}")
            except:
                print("There was a problem with reading the file in viewing")         
        else:
            print("Uuuuummmmmmmmm..... uh oh")
            return
    
    # Function to update item
    def update_item():
        nonlocal library
        nonlocal removed_items
        if csv_has_stuff("Personal_Projects/the_personal_libraray.csv") == False or not library:
            print("You don't have a libaray to edit! Try adding something before removing.")
            return
        while True:
            while True:
                file_choice = input("Would you like to update something in the\n1) run library\nor\n2) saved file").strip().lower()
                if file_choice == "1":
                    break
                elif file_choice == "2":
                    break
                else:
                    print("Invalid input. Try again")
                    continue
            title = input("Title of Book: \n").strip().title()
            author = input("Author of Book:\n").strip().title()
            if file_choice == "1":
                # Updating something in run library
                for item in library:
                    if title in item and author in item:
                        # book meets requirments, ask user if they want to remove it
                        print(f"Found '{item['title']}' by {item['author']}")
                        while True:
                            update = input(f"Do you wish to update '{item['title']}' by {item['author']} (Y/N)?\n").strip().upper()
                            if update == "Y":
                                library.remove(item)
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
                                notes = input("Any notes for this book (if none, put a space)").strip().capitalize()
                                library.append({'title': title, 'author': author, 'publish year': year, 'genre': genre, 'notes': notes})
                                print(f"Update Complete\nReturning to main menu . . .")
                                return
                            elif update == "N":
                                again = input("Would you like to\n1) Return to Main Menu\nor\n2) Do Updating Process again")
                                if again == "2":
                                    update_item()
                                else:
                                    print("Returning to main menu . . .")
                                    return
                            else:
                                print("Invalid input. Try again")
                                continue
                    else:
                        # book does not meet requirements, move to next one
                        pass
                else:
                    print(f"Could not find any books feturing the title '{title}' and author {author}.")
                    try_again = input("Would you like to try the updating process again (Y/N):\n").strip().upper()
                    if try_again == "Y":
                        update_item()
                    else:
                        print("Returning to main menu . . .")
                        return
            elif file_choice == "2":
                # updating something in csv
                try:
                    with open("Personal_Projects/the_personal_libraray.csv", "r+", newline = '') as csv_file:
                        reader = csv.reader(csv_file)
                        for row in reader:
                            if row['title'] == title and row['author'] == author:
                                while True:
                                    print(f"Found: {row}")
                                    updated = input("Do you wish to update it (Y/N)?\n").strip().upper()
                                    if updated == "Y":
                                        # get new information. Read csv, check if row is one we want to change: no, append into list of rows we want to save. yes: dont add it and add updated item to list of rows to write. Rewrite entire file.
                                        pass
                                    elif updated == "N":
                                        again2 = input("Would you like to\n1) Return to Main Menu\nor\n2) Do Updating Process again")
                                        if again2 == "2":
                                            update_item()
                                        else:
                                            print("Returning to main menu . . .")
                                            return
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                except:
                    print("Had trouble reading the file in updating item func")
            else:
                print("The program could not find a book with the title and author you specified, or the libaray section you wanted to edit didn't have the item.\nTry again and check your spelling")
                continue

    # Reload the libary. Current run has a list of things the user wants to add and if this is called, clear the list and dont add it to the csv

    type_print("\nWelcome! In this program, you will be able to catalog all of your books in your very own personal library!\n")

    while True:
        time.sleep(.5)
        type_print("What would you like to do?\n(1) Add Book\n(2) Remove Book\n(3) Update an Item\n(4) View Simple Catalog\n(5) Show Detailed Catalog\n(6) Save Changes\n(7) Reload Library from File\n(8) Leave\n")
        
        choice = input("Enter the number corresponding to what you want to do.\n").strip().upper()
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            # Update item
            pass
        elif choice == "4":
            view_library("simple")
            pass
        elif choice == "5":
            view_library("detailed")
            pass
        elif choice == "6":
            # save
            pass
        elif choice == "7":
            # reload
            pass
        elif choice == "8":
            print("Hope you were able to build an amazing catalog of books!")
            break
        else:
            print("That doesn't seem to be a valid input; please try again.")
            continue

personal_library()