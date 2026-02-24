# File for testing code ideas

try:
    with open('test_file.txt', "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(word_count)
except:
    print("That file can't read")