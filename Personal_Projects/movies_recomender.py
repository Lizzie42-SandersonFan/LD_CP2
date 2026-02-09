# LD 1st Personal Project, Movie Recomender
import time
import csv

# REQUIREMENTS
    # A main function that runs the program and shows a persistent menu.
    # A parser function to load and normalize the provided movie list (CSV) into structured records.
    # Separate filter functions for: genre, director, actor(s), and length.
    # A function that combines selected filters (AND logic by default) and returns matching movies.
    # A function to pretty-print results and a function to print the full movie list.
    # Input validation and helpful error messages; handle missing or malformed movie records gracefully.
    # Allow interactive entry of filter values and length ranges (min/max or comparator).

# HINTS
    # Normalize text to lower-case and trim whitespace for case-insensitive matching.
    # Store multi-valued fields (genres, actors) as lists and match if any element contains the query term.
    # Implement length filtering with min and/or max values (support <, > comparators optionally).
    # If zero matches, suggest relaxing or removing one filter.
    # Provide a small sample movies file in the repo and include unit tests for filter logic.

# FILTER RULES CLARIFICATION
    # Matching is case-insensitive.
    # For genres and actors, match if any element contains the query substring (trim whitespace).
    # Length filter accepts min and/or max (integers). If only one provided, use it as bound.
    # Combine multiple filters using logical AND (movie must satisfy every selected filter).
    # If a movie is missing a field, it does not match a filter for that field.


# CODE
def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

# Main function. Displays menu. Options are: Search, Print EVERYTHING, Exit. Has inner functions
def main():
    movies_found = []
    # The Parser function (Requierment 2)

    # Filter funtion for Genre. This will ask for a genre like "romance" or sm and grab everything that has the genre "Romance" IN IT
    def find_genre():
        genre = input("What is the genre you are looking for (ex: 'Science Fiction,' 'Romance')\n").strip().lower()
        try:
            with open("Personal_Projects/Movies_list.csv", "r") as csv_file:
                content = csv.reader(csv_file)
                headers = next(content)
                rows = []
                for line in content:
                    rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
        except:
            print("Something went wrong with reading the file")

    # Filter for Director. This will take in a name (or part of a name) and find every movie with the name in the DIRECTOR'S name

    # Filter for Actor. Same as director but look in the ACTOR'S name

    # Filter for length. Take in a min and/or max and find the movies that fit in the range. IF no min given, min = 0. IF no max given, max = 200 (Every movie in CSV is shorter than that)
    def length_filter():
        while True:
            min = input("What would you like the minimum length in minutes to be (put a space if you don't want a minimum)\n").strip().lower()
            if min.isdigit() == True:
                min = float(min)
            else:
                pass


    # THE FILTERING INVOLVING STRINGS SHOULD BE ONE FUNCTION
    def string_filter(finding):
        searching = input("")

    # Function that is the one asking for the parameters and will use the results from the calling to get the movies that fit all parameters. Return this list that fit parameters
    def find_filters():
        type_print("Choose the filters you would like to apply (enter them separated by spaces):\n 1) Genre\n2) Director\n3) Actor\n 4) Length (min and/or max)\nExample entry: '1 2 4'")
        filters = input("Type the numbers for your filters:\n").strip().lower()
        #

    # Function to print very nicely

    type_print("Welcome user to a program that will let you search through a catolog of movies!\n")
    while True:
        type_print("What would you like to do:\n1) Search with Parameters\n2) View Entire Movie List\n3) Leave\n")
        action = input("Type the number corresponding to what you want to do:\n").strip().lower()
        if action == "1":
            print("user searching with parameters")
        elif action == "2":
            print("user viewing whole list")
        elif action == "3":
            print("user leaving")
            break
        else:
            print("Invalid input. Please try again")
            continue

# main()
# TESTING INDIVIDUAL PARTS
