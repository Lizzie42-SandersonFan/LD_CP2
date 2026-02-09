# LD 1st Writing Files Notes
import csv

# WRITE ON TEXT FILE
# with open("Notes/reading.txt", "w") as file:
    # file.write("I wrote on my file!\n")

# print("code end")

# APPENDING SO I DONT DELETE EVERYTHING IN MY FILE
# with open("Notes/writing.txt", "a") as file:
    # file.write("This is more on my file!\n")

# print("code end")

# READING AND WRITING AT THE SAME TIME
# with open("Notes\\proof.txt", "r+") as file:
    # content = file.read()
    # content+= "\nI wrote on my file"
    # file.write(content)

# print("code end")

# WRITING TO CSV
# with open("Notes\\sample.csv", "a", newline = '') as csv_file:
    # fieldnames = ['username', 'favorite color']
    # writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    #writer.writeheader()
    # writer.writerow({'username': 'bobby52', 'favorite color': 'red'})
    # writer.writerow({'username': 'bobby57', 'favorite color': 'purple'})
    # writer.writerow({'username': 'bobby67', 'favorite color': 'green'})
    # writer.writerow({'username': 'bobby69', 'favorite color': 'hot pink'})
    # writer.writerow({'username': 'bobby42', 'favorite color': 'black'})

# print("Code is done")

# READING AND WRITING A CSV
with open("Notes\\sample.csv", "r+", newline = '') as csv_file:
    fieldnames = ['username', 'favorite color']
    reader = csv.reader(csv_file)
    # PARSING
    for line in reader:
        print(f"Username: {line[0]} Favorite color: {line[1]}")
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    #writer.writeheader()
    writer.writerow({'username': 'squirrel52', 'favorite color': 'red'})
    writer.writerow({'username': 'squirrel57', 'favorite color': 'purple'})
    writer.writerow({'username': 'squirrel67', 'favorite color': 'green'})
    writer.writerow({'username': 'squirrel69', 'favorite color': 'hot pink'})
    writer.writerow({'username': 'squirrel42', 'favorite color': 'black'})

print("Code is done")