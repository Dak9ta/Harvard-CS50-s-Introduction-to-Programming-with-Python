with open("File I-O/file names/names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())