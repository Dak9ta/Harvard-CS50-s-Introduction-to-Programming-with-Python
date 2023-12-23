name = input("What's your name? ")

with open("File I-O/names.txt", "a") as file:
    file.write(f"{name}\n")