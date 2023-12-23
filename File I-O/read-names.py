with open("File I-O/names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())