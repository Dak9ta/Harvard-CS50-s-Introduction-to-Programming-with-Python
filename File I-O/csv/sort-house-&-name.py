students = []

with open("File I-O/csv/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(", ")
        student = {"name": name, 
                   "house": house}
        students.append(student)
        
def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]
        
for student in sorted(students, key=get_house):
    print(f"{student['name']}, {student['house']}")