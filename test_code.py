# File for testing code ideas

try:
        with open(path, "r") as file:
            content = file.read()
            words = content.split(' ')
            word_count = len(words)
            return word_count
    except:
        print("That file can't read")