# LD 1st Personal Project, Movie Recomender
import time

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

# Main function. Displays menu. Options are: Search, Print EVERYTHING, Exit
def main():
    type_print("Welcome user to a program that will let you search through a catolog of movies!\n")
    while True:
        type_print("What woudl you like to do:\n1) Search with Parameters\n2) Print Entire Movie List\n3) Leave")
        action = input("Type the number corresponding to what you want to do:\n")
        if action == "1":
            pass
        elif action == "2":
            pass
        elif action == "3":
            pass
        else:
            pass


# The Parser function (Requierment 2)

# Filter funtion for Genre. This will ask for a genre like "romance" or sm and grab everything that has the genre "Romance" IN IT

# Filter for Director. This will take in a name (or part of a name) and find every movie with the name in the DIRECTOR'S name

# Filter for Actor. Same as director but look in the ACTOR'S name

# Filter for length. Take in a min and/or max and find the movies that fit in the range. IF no min given, min = 0. IF no max given, max = 200 (Every movie in CSV is shorter than that)

# THE FILTERING INVOLVING STRINGS SHOULD BE ONE FUNCTION

# Function that is the one asking for the parameters and will use the results from the calling to get the movies that fit all parameters. Return this list that fit parameters

# Function to print very nicely