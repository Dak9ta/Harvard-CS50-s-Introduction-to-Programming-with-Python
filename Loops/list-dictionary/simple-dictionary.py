# This is a dictionary, you can stroe information and print it like a list
students = { 
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

for student in students:
    print(student, students[student], sep=": ")