# LD 1st File that will handle accsessing files for Word Counter
from helpers import *
from time_handle import *

# Note by file handling I mean that on ANOTHER page your need to write the code that reads the requested text file, cleans up the input and makes it ready for the user to see/use. 
# It should also handle editing the txt file AND adding the timestamp to the bottom. 

# Function for getting file path. Give example (example is a valid file that I made) and checks if given path is a valid one (it will be put where I want it to)
def get_file_path():
    while True:
        file_path = input("Type in the full path of the file you wish to edit\nEX: 'Personal_Projects/word counter/document.txt'\n")
        if 'Personal_Projects/word counter/' in file_path:
            # File path has what I want for it to be put in the correct spot
            return file_path
        else:
            type_print("Your file path seems to be missing some key words.\nMake sure 'Personal_Projects/word counter/' comes before your file name, and try again")
            continue

# Function for viewing the full file (will need to have the timestamp from time_handle)
def read_file(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            print(content)
    except:
        print("That file can't read")

# Function for adding to file. Will need time_handle help to get timestamp for the editiing
def add_to_file(path):
    try:
        with open(path, "a") as file:
            new_stuff = input("Type what you want added to your file (Hit 'Enter' when you are done):\n")
            file.write(f"{new_stuff}\n")
            update_time = get_time()
            file.write(f"Last Updated at: {update_time}\n")
    except:
        print("That file can't read")

# Function for getting word count. Will need to read current document status, count each word (separated by spaces) and return count
def get_word_count(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except:
        print("That file can't read")
