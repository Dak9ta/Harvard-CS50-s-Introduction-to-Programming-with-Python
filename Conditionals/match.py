# Match is used to select a lot of cases without using the if statement
name = input("What's your name? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _: # This is to select all the cases that are not specified
        print("Who?")