# LD 1st Reading Files Notes
import csv

while True:
    try:
        with open("Notes/reading.txt", "r") as file:
            content = file.read()
            print(content)
    except:
        print("That file can't read")
    else:
        print("Code ends")
        break

try:
    with open("Notes/sample.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0]: line[0], headers[1]: line[1]})
except:
    print("Can't find that file")
else:
    for line in rows:
        print(line)